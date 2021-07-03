coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')


def make_dict(k, v):
    name = {k: v for k, v in zip(k, v)}
    return name


dict_ = make_dict(coin, code)
print(dict_)
