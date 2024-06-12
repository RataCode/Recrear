import pandas as pd

def existencias(SWf1,SWfV1,SWfAL1, SWfCR1, SWfH1, SWfAD1, SWfAIR1, SWfP1):
    bola = False
    if SWf1.any() or SWfV1.any() or SWfAL1.any() or SWfCR1.any() or SWfH1.any() or SWfAD1.any() or SWfAIR1.any() or SWfP1.any():
        bola = True
    return bola
