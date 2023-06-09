"""
SINGLE FILER

Single Filer Income	Tax Rate	Tax Calculation

$0 to $9,950	        10%	10%
$9,951 to $40,525	    12%	$995 plus 12% of income over $9,950
$40,526 to $86,375	    22%	$4,664 plus 22% of income over $40,525
$86,376 to $164,925 	24%	$14,751 plus 24% of income over $86,375
$164,926 to $209,425	32%	$33,603 plus 32% of income over $164,925
$209,426 to $523,600	35%	$47,843 plus 35% of income over $209,425
$523,601 or more	    37%	$157,804.25 plus 37% of income over $523,600

MARRIED FILING JOINTLY

Married Filing Jointly Income	Tax Rate	Tax Calculation

$0 to $19,900           10%	10% of taxable income
$19,901 to $81,050	    12%	$1,990 plus 12% of income over $19,900
$81,051 to $172,750	    22%	$9,328 plus 22% of income over $81,050
$172,751 to $329,850	24%	$29,502 plus 24% of income over $172,750
$329,851 to $418,850	32%	$67,206 plus 32% of income over $329,850
$418,851 to $628,300	35%	$95,686 plus 35% of income over $418,850
$628,301 or more	    37%	$168,993.50 plus 37% of income over $628,300

https://www.payactiv.com/financial-learning/tax-brackets-101-how-your-taxes-are-calculated/

"""
# single_tax_brackets
s_bracket_a = 9950
s_bracket_b = 40525
s_bracket_c = 86375
s_bracket_d = 164925
s_bracket_e = 209425
s_bracket_f = 523600
s_bracket_g = 523601

# calculates what to add from previous tax brackets for single
s_b_a = s_bracket_a*.1
s_b_b = ((s_bracket_b-s_bracket_a)*.12) + s_b_a
s_b_c = ((s_bracket_c-s_bracket_b)*.22) + s_b_b
s_b_d = ((s_bracket_d-s_bracket_c)*.24) + s_b_c
s_b_e = ((s_bracket_e-s_bracket_d)*.32) + s_b_d
s_b_f = ((s_bracket_f-s_bracket_e)*.35) + s_b_e
s_b_g = ((s_bracket_g-s_bracket_f)*.37) + s_b_f

# married_tax_brackets
m_bracket_a = 19900
m_bracket_b = 81050
m_bracket_c = 172750
m_bracket_d = 329850
m_bracket_e = 418850
m_bracket_f = 628300
m_bracket_g = 628301

# calculates what to add from previous tax brackets for married
m_b_a = m_bracket_a*.1
m_b_b = ((m_bracket_b-m_bracket_a)*.12) + m_b_a
m_b_c = ((m_bracket_c-m_bracket_b)*.22) + m_b_b
m_b_d = ((m_bracket_d-m_bracket_c)*.24) + m_b_c
m_b_e = ((m_bracket_e-m_bracket_d)*.32) + m_b_d
m_b_f = ((m_bracket_f-m_bracket_e)*.35) + m_b_e
m_b_g = ((m_bracket_g-m_bracket_f)*.37) + m_b_f

# check what tax bracket for single
def check_income_single_bracket(income):
    if income <= s_bracket_a:
        return 'a'
    elif income > s_bracket_a and income <= s_bracket_b:
        return 'b'
    elif income > s_bracket_b and income <= s_bracket_c:
        return 'c'
    elif income > s_bracket_c and income <= s_bracket_d:
        return 'd'
    elif income > s_bracket_d and income <= s_bracket_e:
        return 'e'
    elif income > s_bracket_e and income <= s_bracket_f:
        return 'f'
    elif income > s_bracket_f:
        return 'g'

# check what tax bracket for married
def check_income_married_bracket(income):
    if income <= m_bracket_a:
        return 'a'
    elif income > m_bracket_a and income <= m_bracket_b:
        return 'b'
    elif income > m_bracket_b and income <= m_bracket_c:
        return 'c'
    elif income > m_bracket_c and income <= m_bracket_d:
        return 'd'
    elif income > m_bracket_d and income <= m_bracket_e:
        return 'e'
    elif income > m_bracket_e and income <= m_bracket_f:
        return 'f'
    elif income > m_bracket_f:
        return 'g'

# calculate taxes single
def calculate_taxes_single(bracket,income):
    match bracket:
        case 'a':
            return income*.1
        case 'b':
            return ((income - s_bracket_a)*.12 + s_b_a)
        case 'c':
            return ((income - s_bracket_b)*.22 + s_b_b)
        case 'd':
            return ((income - s_bracket_c)*.24 + s_b_c)
        case 'e':
            return ((income - s_bracket_d)*.32 + s_b_d) 
        case 'f':
            return ((income - s_bracket_e)*.35 + s_b_e)
        case 'g':
            return ((income - s_bracket_f)*.37 + s_b_f)

# calculate taxes married
def calculate_taxes_married(bracket,income):
    match bracket:
        case 'a':
            return income*.1
        case 'b':
            return ((income - m_bracket_a)*.12 + 1990)
        case 'c':
            return ((income - m_bracket_b)*.22 + 9328)
        case 'd':
            return ((income - m_bracket_c)*.24 + 29502)
        case 'e':
            return ((income - m_bracket_d)*.32 + 67206) 
        case 'f':
            return ((income - m_bracket_e)*.35 + 95686)
        case 'g':
            return ((income - m_bracket_f)*.37 + 168993.50)

# calculates net income, after taxes
def net_income(income,tax):
    return (income - tax)

def run_check(status,income):
    tax_and_net = []
    if status == 'single':
        # if single
        bracket = check_income_single_bracket(income)
        tax = calculate_taxes_single(bracket,income)
        tax_and_net.append(tax)
        tax_and_net.append(net_income(income,tax))
        return tax_and_net
    else:
        # if married
        bracket = check_income_married_bracket(income)
        tax = calculate_taxes_married(bracket,income)
        tax_and_net.append(tax)
        tax_and_net.append(net_income(income,tax))
        net_income(income,tax)
        return tax_and_net
 
#print(run_check('married',40526))