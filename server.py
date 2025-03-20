# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Medical Calculator")


# Converts fructosamine to Hemoglobin A1c
@mcp.tool()
def fructosamine_to_hba1c(fructosamine: int) -> float:
    """Converts fructosamine to Hemoglobin A1c"""
    hba1c = ((0.017 * fructosamine) + 1.61)
    return hba1c

# Additional endocrinology calculator functions
@mcp.tool()
def estimated_average_glucose(hba1c: float) -> float:
    """
    Converts HbA1c to estimated average glucose (eAG) in mg/dL
    Formula: eAG (mg/dL) = 28.7 × HbA1c − 46.7
    """
    return (28.7 * hba1c) - 46.7

@mcp.tool()
def eag_to_hba1c(eag_mg_dl: float) -> float:
    """
    Converts estimated average glucose (eAG) in mg/dL to HbA1c
    Formula: HbA1c = (eAG + 46.7) / 28.7
    """
    return (eag_mg_dl + 46.7) / 28.7

@mcp.tool()
def glucose_unit_conversion_mmol_to_mg(glucose_mmol: float) -> float:
    """
    Converts glucose from mmol/L to mg/dL
    Formula: mg/dL = mmol/L × 18.0182
    """
    return glucose_mmol * 18.0182

@mcp.tool()
def glucose_unit_conversion_mg_to_mmol(glucose_mg: float) -> float:
    """
    Converts glucose from mg/dL to mmol/L
    Formula: mmol/L = mg/dL / 18.0182
    """
    return glucose_mg / 18.0182

@mcp.tool()
def bmi_calculator(weight_kg: float, height_m: float) -> float:
    """
    Calculates Body Mass Index (BMI)
    Formula: BMI = weight (kg) / height^2 (m)
    """
    return weight_kg / (height_m * height_m)

@mcp.tool()
def ideal_body_weight(height_cm: float, is_male: bool) -> float:
    """
    Calculates Ideal Body Weight (IBW) in kg using the Devine formula
    For males: IBW = 50 + 2.3 × (height in inches - 60)
    For females: IBW = 45.5 + 2.3 × (height in inches - 60)
    """
    height_inches = height_cm / 2.54
    if is_male:
        return 50 + 2.3 * (height_inches - 60)
    else:
        return 45.5 + 2.3 * (height_inches - 60)

@mcp.tool()
def corrected_calcium(calcium: float, albumin: float) -> float:
    """
    Calculates corrected calcium level
    Formula: Corrected calcium (mg/dL) = measured calcium (mg/dL) + 0.8 * (4.0 - albumin (g/dL))
    """
    return calcium + 0.8 * (4.0 - albumin)

@mcp.tool()
def free_androgen_index(total_testosterone: float, shbg: float) -> float:
    """
    Calculates Free Androgen Index (FAI)
    Formula: FAI = (total testosterone / SHBG) * 100
    Where:
    - total testosterone in nmol/L
    - SHBG in nmol/L
    """
    return (total_testosterone / shbg) * 100



@mcp.tool()
def insulin_correction_factor(tdd: float) -> float:
    """
    Calculates insulin correction factor (ICF) or insulin sensitivity factor
    Formula: 1800 / TDD (using 1800 rule)
    """
    return 1800 / tdd

@mcp.tool()
def insulin_to_carb_ratio(tdd: float) -> float:
    """
    Calculates insulin to carbohydrate ratio (I:C)
    Formula: 450 / TDD (using 450 rule)
    """
    return 450 / tdd

@mcp.tool()
def calculate_egfr(creatinine: float, age: int, is_male: bool, is_black: bool) -> float:
    """
    Calculates estimated Glomerular Filtration Rate (eGFR) using the MDRD formula
    Formula: 175 × (Scr)^-1.154 × (Age)^-0.203 × (0.742 if female) × (1.212 if black)
    Where Scr is serum creatinine in mg/dL
    """
    egfr = 175 * (creatinine ** -1.154) * (age ** -0.203)
    
    if not is_male:
        egfr *= 0.742
    if is_black:
        egfr *= 1.212
    
    return egfr
