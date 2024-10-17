import os
import sys

current_dir = os.path.dirname(__file__)
sys.path.append(current_dir)

from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.filters import Text
from answers import SOFT, LEGAL_COMMENT, LEGAL_1, LEGAL_MAIN, LEGAL_2, BP_MAIN, BP_MARKET_ANALYSIS, BP_AD_CAMPAIGN, \
    BP_CUSTOMER_SERVICE, BP_COMMENT, BP_ORG_PLAN, BP_RISK_ANALYSIS, BP_FINANCIAL_PLAN_NO_kb, BP_FINANCIAL_PLAN_kb, \
    BP_FP_U_M_ARPU
from keyboards import kb_soft, kb_start, kb_legal0, kb_legal1, kb_legal2, leg_keys_main, kb_bp0, bp_main_keys, kb_bp1, \
    kb_bp_ma, kb_bp_AdCamp, kb_bp_CustSer, kb_bp_OrgPlan, kb_bp_RiskAn, kb_bp_FinPlan, bp_FinPlan_keys_add, \
    kb_bp_Margin, kb_bp_ARPU, kb_bp_Unit

TOKEN_API = '6905548076:AAEKal7jmZnJdlb6ieiCWrR_6WydxkhQB2w'
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Я работаю!")


@dp.message_handler(commands=['start'])
async def start_com(message: types.Message):
    name = message.from_user.first_name
    await message.answer(text=f"Здравствуйте, {name}! 👋\nЯ Ваш помощник в мире продавцов ВБ.\nК какой теме относится ваш вопрос?",
                         reply_markup=kb_start)
    await message.delete()


@dp.message_handler(Text(equals="Юридическая составляющая"))
async def legal_com(message: types.Message):
    await message.answer(text=LEGAL_COMMENT, reply_markup=kb_legal0)


@dp.message_handler(Text(equals=leg_keys_main[0]))
async def legal_m1_com(message: types.Message):
    await message.answer(text=LEGAL_MAIN.get(leg_keys_main[0]), reply_markup=kb_legal1)


@dp.message_handler(Text(equals=leg_keys_main[1]))
async def legal_m2_com(message: types.Message):
    await message.answer(text=LEGAL_MAIN.get(leg_keys_main[1]), reply_markup=kb_legal2)


@dp.message_handler(Text(equals=leg_keys_main[2]))
async def legal_m3_com(message: types.Message):
    await message.answer(text=LEGAL_MAIN.get(leg_keys_main[2]))

for key in LEGAL_1:
    @dp.message_handler(Text(equals=key))
    async def legal1_dict(message: types.Message):
        await message.answer(text=LEGAL_1.get(message.text), parse_mode="HTML")


for key in LEGAL_2:
    @dp.message_handler(Text(equals=key))
    async def legal2_dict(message: types.Message):
        await message.answer(text=LEGAL_2.get(message.text), parse_mode="HTML")


@dp.message_handler(Text(equals="Бизнес-план"))
async def BP_com(message: types.Message):
    await message.answer(
        text="В данном разделе я расскажу, что такое бизнес-план и как его правильно составить.",
        reply_markup=kb_bp0)


@dp.message_handler(Text(equals=bp_main_keys[0]))
async def bp_m1_com(message: types.Message):
    await message.answer(text=BP_MAIN.get(bp_main_keys[0]))


@dp.message_handler(Text(equals=bp_main_keys[1]))
async def bp_m2_com(message: types.Message):
    await message.answer(text=BP_MAIN.get(bp_main_keys[1]), reply_markup=kb_bp1)


@dp.message_handler(Text(equals="Анализ рынка"))
async def bp_ma_com(message: types.Message):
    await message.answer(text=BP_COMMENT.get("Анализ рынка"), reply_markup=kb_bp_ma)

for key in BP_MARKET_ANALYSIS:
    @dp.message_handler(Text(equals=key))
    async def ma_dict(message: types.Message):
        await message.answer(text=BP_MARKET_ANALYSIS.get(message.text), parse_mode="HTML")


@dp.message_handler(Text(equals="Продвижение товаров – рекламные кампании"))
async def bp_AdCamp_com(message: types.Message):
    await message.answer(text=BP_COMMENT.get("Продвижение товаров – рекламные кампании"), reply_markup=kb_bp_AdCamp)


for key in BP_AD_CAMPAIGN:
    @dp.message_handler(Text(equals=key))
    async def AdCamp_dict(message: types.Message):
        await message.answer(text=BP_AD_CAMPAIGN.get(message.text), parse_mode="HTML")


@dp.message_handler(Text(equals="Обслуживание покупателей и обратная связь"))
async def bp_CustSer_com(message: types.Message):
    await message.answer(text=BP_COMMENT.get("Обслуживание покупателей и обратная связь"), reply_markup=kb_bp_CustSer)


for key in BP_CUSTOMER_SERVICE:
    @dp.message_handler(Text(equals=key))
    async def CustSer_dict(message: types.Message):
        await message.answer(text=BP_CUSTOMER_SERVICE.get(message.text), parse_mode="HTML")


@dp.message_handler(Text(equals="Организационный план"))
async def bp_OrgPlan_com(message: types.Message):
    await message.answer(text=BP_COMMENT.get("Организационный план"), reply_markup=kb_bp_OrgPlan)

for key in BP_ORG_PLAN:
    @dp.message_handler(Text(equals=key))
    async def OrgPlan_dict(message: types.Message):
        await message.answer(text=BP_ORG_PLAN.get(message.text), parse_mode="HTML")


@dp.message_handler(Text(equals="Финансовый план"))
async def bp_FinPlan_com(message: types.Message):
    await message.answer(text=BP_COMMENT.get("Финансовый план"), reply_markup=kb_bp_FinPlan)


for key in BP_FINANCIAL_PLAN_NO_kb:
    @dp.message_handler(Text(equals=key))
    async def FinPlan_dict(message: types.Message):
        await message.answer(text=BP_FINANCIAL_PLAN_NO_kb.get(message.text), parse_mode="HTML")


@dp.message_handler(Text(equals=bp_FinPlan_keys_add[0]))
async def bp_Unit_com(message: types.Message):
    await message.answer(text=BP_FINANCIAL_PLAN_kb.get(bp_FinPlan_keys_add[0]), reply_markup=kb_bp_Unit)


@dp.message_handler(Text(equals=bp_FinPlan_keys_add[1]))
async def bp_Margin_com(message: types.Message):
    await message.answer(text=BP_FINANCIAL_PLAN_kb.get(bp_FinPlan_keys_add[1]), reply_markup=kb_bp_Margin)


@dp.message_handler(Text(equals=bp_FinPlan_keys_add[2]))
async def bp_ARPU_com(message: types.Message):
    await message.answer(text=BP_FINANCIAL_PLAN_kb.get(bp_FinPlan_keys_add[2]), reply_markup=kb_bp_ARPU)

for key in BP_FP_U_M_ARPU:
    @dp.message_handler(Text(equals=key))
    async def U_M_ARPU_dict(message: types.Message):
        await message.answer(text=BP_FP_U_M_ARPU.get(message.text), parse_mode="HTML")


@dp.message_handler(Text(equals="Анализ рисков"))
async def bp_RiskAn_com(message: types.Message):
    await message.answer(text=BP_COMMENT.get("Анализ рисков"), reply_markup=kb_bp_RiskAn)

for key in BP_RISK_ANALYSIS:
    @dp.message_handler(Text(equals=key))
    async def RiskAn_dict(message: types.Message):
        await message.answer(text=BP_RISK_ANALYSIS.get(message.text), parse_mode="HTML")

@dp.message_handler(Text(equals="Софт"))
async def soft_com(message: types.Message):
    await message.answer(text="В данном разделе я расскажу, какие инструменты можно использовать для автоматизации расчета",
                         reply_markup=kb_soft)


for key in SOFT:
    @dp.message_handler(Text(equals=key))
    async def soft_dict(message: types.Message):
        await message.answer(text=SOFT.get(message.text), parse_mode="HTML")


@dp.message_handler(Text(equals="Главное меню"))
async def main_menu(message: types.Message):
    await message.answer(text="Какая тема вас интересует?",
                         reply_markup=kb_start)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)

