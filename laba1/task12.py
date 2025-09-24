
BASE_PRICE = 24.99
INCLUDED_MINUTES = 60
INCLUDED_SMS = 30
INCLUDED_MB = 1024


EXTRA_MINUTE_PRICE = 0.89
EXTRA_SMS_PRICE = 0.59
EXTRA_MB_PRICE = 0.79


TAX_RATE = 0.02


used_minutes = int(input("Введите количество израсходованных минут: "))
used_sms = int(input("Введите количество израсходованных SMS: "))
used_mb = int(input("Введите количество израсходованных МБ: "))


extra_minutes = max(0, used_minutes - INCLUDED_MINUTES)
extra_sms = max(0, used_sms - INCLUDED_SMS)
extra_mb = max(0, used_mb - INCLUDED_MB)


base_sum = BASE_PRICE
extra_minutes_sum = extra_minutes * EXTRA_MINUTE_PRICE
extra_sms_sum = extra_sms * EXTRA_SMS_PRICE
extra_mb_sum = extra_mb * EXTRA_MB_PRICE


total_before_tax = base_sum + extra_minutes_sum + extra_sms_sum + extra_mb_sum


tax_amount = total_before_tax * TAX_RATE
total_amount = total_before_tax + tax_amount


print("\n--- Чек за мобильную связь ---")
print(f"Базовая сумма тарификации: {base_sum:.2f} руб.")

if extra_minutes > 0:
    print(f"Дополнительные минуты ({extra_minutes} мин.): {extra_minutes_sum:.2f} руб.")

if extra_sms > 0:
    print(f"Дополнительные SMS ({extra_sms} шт.): {extra_sms_sum:.2f} руб.")

if extra_mb > 0:
    print(f"Дополнительный трафик ({extra_mb} МБ): {extra_mb_sum:.2f} руб.")

print(f"Налог (2%): {tax_amount:.2f} руб.")
print(f"Итоговая сумма к оплате: {total_amount:.2f} руб.")