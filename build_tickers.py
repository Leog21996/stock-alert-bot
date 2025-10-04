import pandas as pd
import requests
from io import StringIO

def get_sp500_tickers():
    url = "https://datahub.io/core/s-and-p-500-companies/r/constituents.csv"
    response = requests.get(url)
    response.raise_for_status()
    df = pd.read_csv(StringIO(response.text))
    return df['Symbol'].tolist()

DJIA = [
    "AAPL", "AMGN", "AXP", "BA", "CAT", "CSCO", "CVX", "DIS", "DOW", "GS",
    "HD", "IBM", "INTC", "JNJ", "JPM", "KO", "MCD", "MMM", "MRK", "MSFT",
    "NKE", "PG", "CRM", "TRV", "UNH", "V", "VZ", "WMT", "WBA"
]

NASDAQ_100 = [
    "AAPL", "ADBE", "AMAT", "AMGN", "AMZN", "ANSS", "ASML", "ATVI", "AVGO", "BIDU",
    "BIIB", "BKNG", "CDNS", "CDW", "CERN", "CHKP", "CHTR", "CMCSA", "COST", "CSCO",
    "CSX", "CTAS", "CTSH", "DLTR", "DOCU", "DXCM", "EA", "EBAY", "EXC", "FAST",
    "FB", "FISV", "FOX", "FOXA", "GILD", "GOOG", "GOOGL", "HAS", "HSIC", "IDXX",
    "ILMN", "INCY", "INTC", "INTU", "ISRG", "JD", "KHC", "KLAC", "LBTYA", "LBTYK",
    "LULU", "MAR", "MDLZ", "MNST", "MSFT", "MU", "MXIM", "NFLX", "NVDA", "NXPI",
    "OKTA", "ORLY", "PAYX", "PCAR", "PEP", "PDD", "PYPL", "QCOM", "REGN", "ROST",
    "SBUX", "SGEN", "SIRI", "SNPS", "SWKS", "TCOM", "TSLA", "TXN", "VRSK", "VRTX",
    "WBA", "WDAY", "XEL", "XLNX", "ZM"
]

FTSE_MIB = [
    "A2A.MI", "AMPL.MI", "AZM.MI", "BAMI.MI", "BPE.MI", "BPMI.MI", "CNHI.MI", "ENEL.MI",
    "ENI.MI", "EXO.MI", "FCA.MI", "G.MI", "GFT.MI", "HERA.MI", "ISP.MI", "IT.MI", "LDO.MI",
    "LUX.MI", "MONC.MI", "MS.MI", "P.MI", "PIRC.MI", "POST.MI", "REC.MI", "S.MI", "SRG.MI",
    "ST.MI", "STT.MI", "TLIT.MI", "UG.MI", "UCG.MI", "UBI.MI", "UNI.MI", "Z.MI"
]

DAX = [
    "ADS.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BMW.DE", "BOS.DE", "CON.DE", "DAI.DE",
    "DBK.DE", "DPW.DE", "DTE.DE", "EOAN.DE", "FME.DE", "FRE.DE", "HEI.DE", "HEN3.DE",
    "IFX.DE", "LIN.DE", "MRK.DE", "MTX.DE", "MUV2.DE", "RWE.DE", "SAP.DE", "SIE.DE",
    "VOW3.DE", "VNA.DE"
]

FTSE_100 = [
    "AAL.L", "ADM.L", "AHT.L", "ANTO.L", "AZN.L", "BA.L", "BARC.L", "BATS.L", "BDEV.L", "BHP.L",
    "BP.L", "BRBY.L", "CCH.L", "CCL.L", "CNA.L", "CRH.L", "DGE.L", "EVR.L", "EXPN.L", "FRES.L",
    "GSK.L", "HL.L", "HSBA.L", "IMB.L", "INF.L", "ITRK.L", "JMAT.L", "KGF.L", "LAND.L", "LGEN.L",
    "LLOY.L", "LSE.L", "MNG.L", "MRO.L", "NG.L", "NXT.L", "OCN.L", "PSON.L", "PSN.L", "RDSA.L",
    "RDSB.L", "REL.L", "RIO.L", "RR.L", "SBRY.L", "SGE.L", "SMT.L", "SN.L", "SPX.L", "TSCO.L",
    "ULVR.L", "VOD.L", "WPP.L"
]

CAC_40 = [
    "AIR.PA", "AI.PA", "ALU.PA", "AM.PA", "AXA.PA", "BN.PA", "BNP.PA", "BOUY.PA", "CAP.PA", "CS.PA",
    "DANO.PA", "DSY.PA", "ENGI.PA", "ESSI.PA", "EUF.PA", "KER.PA", "LHN.PA", "LVMH.PA", "MC.PA", "ML.PA",
    "OR.PA", "PUB.PA", "RMS.PA", "SAF.PA", "SAN.PA", "SGO.PA", "STM.PA", "SU.PA", "SW.PA", "VIE.PA"
]

def save_tickers(filename="tickers.py"):
    sp500_tickers = get_sp500_tickers()
    with open(filename, "w") as f:
        f.write("# Ticker dei principali indici globali\n\n")
        f.write("S_P_500 = " + str(sp500_tickers) + "\n\n")
        f.write("DJIA = " + str(DJIA) + "\n\n")
        f.write("NASDAQ_100 = " + str(NASDAQ_100) + "\n\n")
        f.write("FTSE_MIB = " + str(FTSE_MIB) + "\n\n")
        f.write("DAX = " + str(DAX) + "\n\n")
        f.write("FTSE_100 = " + str(FTSE_100) + "\n\n")
        f.write("CAC_40 = " + str(CAC_40) + "\n\n")
    print(f"File {filename} creato con successo!")

if __name__ == "__main__":
    save_tickers()