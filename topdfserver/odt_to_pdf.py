import os
import subprocess


def unoconv_exists():
    result = subprocess.call(['which', 'unoconv'])
    if result == 0:
        return True
    else:
        return False


def register(converters, unoconv_exists=unoconv_exists):
    if unoconv_exists():
        converters['application/vnd.oasis.opendocument.text'] = odt_to_pdf


def odt_to_pdf(filepath, target_dir):
    command = ['unoconv', '-o', target_dir, '--format', 'pdf',
        filepath]
    subprocess.call(command)
    basename = os.path.basename(filepath)
    filename, ext = os.path.splitext(basename)
    return os.path.join(target_dir, filename + '.pdf')