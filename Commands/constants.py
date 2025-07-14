import win32print

FONT_BASE = "Tahoma"

PRINTERS = []
for printer in win32print.EnumPrinters(2):
    PRINTERS.append(printer[2])

POSITION_LIST = [
    '1º', '2º', '3º', '4º', '5º', '6º', '7º', '8º', '9º',
    '10º', '11º', '12º', '13º', '14º', '15º', '16º', '17º',
    '18º', '19º', '20º', '21º', '22º', '23º', '24º', '25º']

PROCEDIMENT_LIST = [
    'Banho e Higiênica', 'Tosa Padrão 7', 'Tosa Padrão 10',
    'Tosa Completa 7', 'Tosa Completa 10', 'Tosa Bebê']

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "impressora": "default",
    "path_dir": "./comandas"
}
