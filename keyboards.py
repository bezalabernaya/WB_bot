from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from answers import LEGAL_1, LEGAL_MAIN, BP_MAIN, BP_MARKET_ANALYSIS, BP_AD_CAMPAIGN, BP_CUSTOMER_SERVICE, BP_ORG_PLAN, BP_RISK_ANALYSIS, BP_FINANCIAL_PLAN_NO_kb, BP_FINANCIAL_PLAN_kb, BP_FP_U_M_ARPU

kb_start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton(text="Юридическая составляющая")
b2 = KeyboardButton(text="Бизнес-план")
b3 = KeyboardButton(text="Софт")
kb_start.add(b1).add(b2).add(b3)

kb_soft = ReplyKeyboardMarkup(resize_keyboard=True)
kb_soft.add(KeyboardButton(text="Калькулятор Webhelp")).add(KeyboardButton(text="Проект WBCON.RU")).add(KeyboardButton(text="Платформа Product Star")).add(KeyboardButton(text="Главное меню"))

leg_keys_main = list(LEGAL_MAIN.keys())

kb_legal0 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_legal0.add(KeyboardButton(text=leg_keys_main[0])).add(KeyboardButton(text=leg_keys_main[1])).add(KeyboardButton(text=leg_keys_main[2])).add(KeyboardButton(text="Главное меню"))

leg_keys = list(LEGAL_1.keys())

kb_legal1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_legal1.add(KeyboardButton(text=leg_keys[0])).add(KeyboardButton(text=leg_keys[1])).add(KeyboardButton(text=leg_keys[2])).add(KeyboardButton(text=leg_keys[3])).add(KeyboardButton(text=leg_keys[4])).add(KeyboardButton(text=leg_keys[5])).add(KeyboardButton(text="Главное меню"))

kb_legal2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_legal2.add(KeyboardButton(text="Нужен ли бухгалтер для ИП?")).add(KeyboardButton(text="Нужен ли бухгалтер для самозанятого?")).add(KeyboardButton(text="Главное меню"))

bp_main_keys = list(BP_MAIN.keys())

kb_bp0 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp0.add(KeyboardButton(text=bp_main_keys[0])).add(KeyboardButton(text=bp_main_keys[1]))

kb_bp1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp1.add(KeyboardButton(text="Анализ рынка")).add(KeyboardButton(text="Продвижение товаров – рекламные кампании")).add(KeyboardButton(text="Обслуживание покупателей и обратная связь")).add(KeyboardButton(text="Организационный план")).add(KeyboardButton(text="Финансовый план")).add(KeyboardButton(text="Анализ рисков")).add(KeyboardButton(text="Главное меню"))

bp_ma_keys = list(BP_MARKET_ANALYSIS.keys())
kb_bp_ma = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_ma.add(KeyboardButton(text=bp_ma_keys[0])).add(KeyboardButton(text=bp_ma_keys[1])).add(KeyboardButton(text=bp_ma_keys[2])).add(KeyboardButton(text=bp_ma_keys[3])).add(KeyboardButton(text=bp_ma_keys[4])).add(KeyboardButton(text=bp_ma_keys[5])).add(KeyboardButton(text="Главное меню"))

bp_AdCamp_keys = list(BP_AD_CAMPAIGN.keys())
kb_bp_AdCamp = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_AdCamp.add(KeyboardButton(text=bp_AdCamp_keys[0])).add(KeyboardButton(text=bp_AdCamp_keys[1])).add(KeyboardButton(text=bp_AdCamp_keys[2])).add(KeyboardButton(text=bp_AdCamp_keys[3])).add(KeyboardButton(text=bp_AdCamp_keys[4])).add(KeyboardButton(text=bp_AdCamp_keys[5])).add(KeyboardButton(text=bp_AdCamp_keys[6])).add(KeyboardButton(text=bp_AdCamp_keys[7])).add(KeyboardButton(text=bp_AdCamp_keys[8])).add(KeyboardButton(text="Главное меню"))

bp_CusSer_keys = list(BP_CUSTOMER_SERVICE.keys())
kb_bp_CustSer = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_CustSer .add(KeyboardButton(text=bp_CusSer_keys[0])).add(KeyboardButton(text=bp_CusSer_keys[1])).add(KeyboardButton(text=bp_CusSer_keys[2])).add(KeyboardButton(text=bp_CusSer_keys[3])).add(KeyboardButton(text="Главное меню"))

bp_OrgPlan_keys = list(BP_ORG_PLAN.keys())
kb_bp_OrgPlan = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_OrgPlan .add(KeyboardButton(text=bp_OrgPlan_keys[0])).add(KeyboardButton(text=bp_OrgPlan_keys[1])).add(KeyboardButton(text=bp_OrgPlan_keys[2])).add(KeyboardButton(text=bp_OrgPlan_keys[3])).add(KeyboardButton(text="Главное меню"))

bp_RiskAn_keys = list(BP_RISK_ANALYSIS.keys())
kb_bp_RiskAn = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_RiskAn.add(KeyboardButton(text=bp_RiskAn_keys[0])).add(KeyboardButton(text=bp_RiskAn_keys[1])).add(KeyboardButton(text=bp_RiskAn_keys[2])).add(KeyboardButton(text=bp_RiskAn_keys[3])).add(KeyboardButton(text="Главное меню"))

bp_FinPlan_keys = list(BP_FINANCIAL_PLAN_NO_kb.keys())
bp_FinPlan_keys_add = list(BP_FINANCIAL_PLAN_kb.keys())
kb_bp_FinPlan = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_FinPlan.add(KeyboardButton(text=bp_FinPlan_keys[0])).add(KeyboardButton(text=bp_FinPlan_keys[1])).add(KeyboardButton(text=bp_FinPlan_keys[2])).add(KeyboardButton(text=bp_FinPlan_keys[3])).add(KeyboardButton(text=bp_FinPlan_keys[4])).add(KeyboardButton(text=bp_FinPlan_keys[5])).add(KeyboardButton(text=bp_FinPlan_keys[6])).add(KeyboardButton(text=bp_FinPlan_keys_add[0])).add(KeyboardButton(text=bp_FinPlan_keys_add[1])).add(KeyboardButton(text=bp_FinPlan_keys_add[2])).add(KeyboardButton(text="Главное меню"))

bp_U_M_A_keys = list(BP_FP_U_M_ARPU.keys())
kb_bp_Unit = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_Unit.add(KeyboardButton(text=bp_U_M_A_keys[0])).add(KeyboardButton(text=bp_U_M_A_keys[1])).add(KeyboardButton(text=bp_U_M_A_keys[2])).add(KeyboardButton(text=bp_U_M_A_keys[3])).add(KeyboardButton(text=bp_U_M_A_keys[4])).add(KeyboardButton(text="Главное меню"))

kb_bp_Margin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_Margin.add(KeyboardButton(text=bp_U_M_A_keys[5])).add(KeyboardButton(text=bp_U_M_A_keys[6])).add(KeyboardButton(text="Главное меню"))

kb_bp_ARPU = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bp_ARPU.add(KeyboardButton(text=bp_U_M_A_keys[7])).add(KeyboardButton(text=bp_U_M_A_keys[8])).add(KeyboardButton(text=bp_U_M_A_keys[9])).add(KeyboardButton(text=bp_U_M_A_keys[10])).add(KeyboardButton(text="Главное меню"))