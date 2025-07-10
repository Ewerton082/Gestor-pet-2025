import win32print

FONT_BASE = "Tahoma"

PRINTERS = []
for printer in win32print.EnumPrinters(2):
    PRINTERS.append(printer[2])