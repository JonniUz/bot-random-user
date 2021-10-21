from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from .randomer import respon


@dp.message_handler(Command(['random_user']))
async def bot_help(message: types.Message):
    first_name = respon()['name']['first']
    last_name = respon()['name']['first']
    home_num = respon()['location']['street']['number']
    home_name = respon()['location']['street']['name']
    city = respon()['location']['city']
    state = respon()['location']['state']
    country = respon()['location']['country']
    email = respon()['email']
    profile_pic = respon()['picture']['large']
    nat = respon()['nat']

    text = f'Name: {first_name} {last_name}\n'
    text += f'Address: {home_num}, {home_name}, {city}, {state}, {country}\n'
    text += f'Email: {email}\n'
    text += f'Nationality: {nat}'

    await message.answer_document(profile_pic, caption=text)
