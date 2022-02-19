from fman import DirectoryPaneCommand, show_alert
from fman.url import as_human_readable, splitscheme
from fman.fs import resolve
from fman.clipboard import set_text
import subprocess

class Sha256Sum(DirectoryPaneCommand):
    def __call__(self):
        url = self.pane.get_file_under_cursor() 
        if not url:
            show_alert( "Nenhum arquivo pdf selecionado" )
            return
        url = resolve(url)
        scheme = splitscheme(url)[0]
        if scheme != 'file://':
            show_alert( "Não é possível ler o arquivo %s" % scheme )
            return
        filename = as_human_readable(url)
        out = subprocess.check_output(['sha256sum', filename ]).decode('utf-8')
        set_text(out)
        show_alert(out)
