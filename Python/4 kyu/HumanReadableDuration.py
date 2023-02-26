"""
Human Readable Duration Format
https://www.codewars.com/kata/52742f58faf5485cae000b9a
"""

def format_duration(seconds):
    elements = []
    if seconds >= 31536000:
        elements.append(str(seconds // 31536000) + " years" if seconds // 31536000 > 1 else "1 year")
        seconds -= seconds // 31536000 * 31536000
        
    if seconds >= 86400:
        elements.append(str(seconds // 86400) + " days" if seconds // 86400 > 1 else "1 day")
        seconds -= seconds // 86400 * 86400 
        
    if seconds >= 3600:
        elements.append(str(seconds // 3600) + " hours" if seconds // 3600 > 1 else "1 hour")
        seconds -= seconds // 3600 * 3600
        
    if seconds >= 60:
        elements.append(str(seconds // 60) + " minutes" if seconds // 60 > 1 else "1 minute")
        seconds -= seconds // 60 * 60
        
    if seconds >= 1:
        elements.append(str(seconds) + " seconds" if seconds > 1 else "1 second")
        
    if len(elements) > 1: return ", ".join(elements[0:len(elements)-1]) + " and " + elements[len(elements)-1]
    if len(elements) == 1: return elements[0]
    return "now"
