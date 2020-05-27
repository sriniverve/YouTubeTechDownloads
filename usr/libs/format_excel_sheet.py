from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, colors

def cellFormat(cell, cellColor='FFFFFF', fontSize=10, bold=False, fontColor='000000',wrapText=False):
    cell.fill = PatternFill(start_color=cellColor, end_color=cellColor)
    cell.font = Font(size=fontSize, bold=bold, color=fontColor)
    cell.alignment = Alignment(wrap_text=wrapText)