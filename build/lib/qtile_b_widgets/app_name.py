from typing import Any, List, Tuple
from libqtile.widget import base
from libqtile import hook, pangocffi


class AppName(base._TextBox):

    defaults: List[Tuple[str, Any, str]] = [
        ('default_name', '', 'Name to use incase none is detected'),
        ('format', '{name}', 'format of the text'),
    ]

    def __init__(self, **config) -> None:
        base._TextBox.__init__(self, '', **config)
        self.add_defaults(AppName.defaults)

    def _configure(self, qtile, bar) -> None:
        base._TextBox._configure(self, qtile, bar)
        self._setup_hooks()

    def _setup_hooks(self) -> None:
        hook.subscribe.startup(self._update_name)
        hook.subscribe.focus_change(self._update_name)

    def _remove_hooks(self):
        hook.unsubscribe.startup(self._update_name)
        hook.unsubscribe.focus_change(self._update_name)

    def _update_name(self) -> None:
        window = self.qtile.current_screen.group.current_window
        name = window.get_wm_class()[0].capitalize(
        ) if window else self.default_name
        name = name if name else self.default_name
        var = {'name': name}
        unescaped = self.fmt.format(self.format.format(**var))
        self.update(pangocffi.markup_escape_text(unescaped))

    def finalize(self):
        self._remove_hooks()
        base._TextBox.finalize(self)
