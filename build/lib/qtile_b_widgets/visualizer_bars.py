from libqtile.widget import base
import subprocess
import psutil
import os
import textwrap


class VisualizerBars(base.ThreadPoolText):

    defaults = [
        ('pipe', '~/.config/qtile/.gen/cava.fifo',
         'Pipe where cava should dump ascii output'),
        ('config_dump', '~/.config/qtile/.gen/cava.config',
         'Where to dumps config to be used by cava'),
        ('frequency', 60, 'The poll frequency'),
        ('bars', '▁▂▃▄▅▆▇█', 'Characters used to draw the bars'),
        ('bar_count', 10, 'Number of bars'),
    ]

    def __init__(self, **config) -> None:
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(VisualizerBars.defaults)

    def _configure(self, qtile, bar) -> None:
        self.update_interval = 0.5/self.frequency
        base.ThreadPoolText._configure(self, qtile, bar)
        self._create_config()
        self._resume_cava()

    def finalize(self):
        self._kill_cava()
        base.ThreadPoolText.finalize()

    def create_bars(self, level_code: str) -> str:
        return ''.join([self.bars[int(c)] for c in level_code.split(';') if c])

    def poll(self) -> str:
        line = self.pipe_stream.stdout.readline()
        line = line if line else '0;'*self.bar_count
        return self.create_bars(line.strip().decode('utf-8'))

    def _create_config(self) -> None:
        with open(os.path.expanduser(self.config_dump), "w") as f:
            f.write(textwrap.dedent(f'''
                [general]
                bars = {self.bar_count}
                framerate = {self.frequency}
                autosens = 1
                overshoot = 10
                [output]
                method = raw
                raw_target = {os.path.expanduser(self.pipe)}
                data_format = ascii
                ascii_max_range = {len(self.bars) - 1}
                style = stereo
                [smoothing]
                monstercat = 1
                ignore = 1
                [eq]
                1 = 1 # bass
                2 = 1
                3 = 1 # midtone
                4 = 1
                5 = 1 # treble'''))

    def _resume_cava(self) -> None:
        pipe = os.path.expanduser(self.pipe)
        config = os.path.expanduser(self.config_dump)

        if not self._is_cava_running():
            if os.path.exists(pipe):
                os.remove(pipe)
            os.mkfifo(pipe)
            self.cava = psutil.Popen(
                ['cava', '-p', config], stdout=subprocess.PIPE)
        if not self._is_stream_open():
            self.pipe_stream = psutil.Popen(
                ['cat', pipe], stdout=subprocess.PIPE)

    def _kill_cava(self) -> None:
        if self._is_cava_running():
            self.cava.kill()
        if self._is_stream_open():
            self.pipe_stream.kill()

    def _is_cava_running(self):
        try:
            return self.cava.is_running()
        except AttributeError:
            return False

    def _is_stream_open(self):
        try:
            return self.pipe_stream.is_running()
        except AttributeError:
            return False
