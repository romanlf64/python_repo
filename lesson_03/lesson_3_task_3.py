from address import Address
from mailing import Mailing

from_address = Address('636840', 'Асино', 'Ленина', '33', '20')
to_address = Address('656481', 'Санкт-Петербург', 'Пулковская', '23', '303')
mail = Mailing(from_address, to_address, 1200, 'track345')

print(mail)
