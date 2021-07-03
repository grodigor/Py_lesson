def is_date(y, m, d):
    import datetime
    try:
        datetime.date(y, m, d)
        return True
    except:
        return False
