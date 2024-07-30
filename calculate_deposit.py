def calculate_deposit(principal, periods, interest_rate):
  """計算定存本利和

  Args:
    principal: 初始本金
    periods: 期數
    interest_rate: 年利率

  Returns:
    期滿後本利和
  """

  # 複利計算公式
  amount = principal * (1 + interest_rate/100) ** periods 
    # ** 次方
  
  # 四捨五入至整數，並加上千分位符號
  formatted_amount = f"{amount:,.0f}"
    # f"： 表示 f-字串
    # {amount}： 插入變數amount的值
    # ,： 在數字中插入千分位分隔符號
    # .0f： 取整數保留小數點後0位
  return formatted_amount

# 輸入參數
principal = 500000
periods = 24
interest_rate = 6

# 輸出結果  2,024,467
result = calculate_deposit(principal, periods, interest_rate)
print(result)

