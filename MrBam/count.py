from collections import Counter

def count_different_type(o, pairs, single, alt, ref):
    mor, mnr, msr, oor, onr, osr, moa, mna, msa, ooa, ona, osa, inconsis = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

    if ref=='-' or any(len(x) > 1 for x in alt):
        alt, ref = 'I', 'ATCG'
    elif alt=='-' or len(ref) >= 2:
        alt, ref = 'D', 'ATCG'

    for (*_, overlaped), reads in pairs.items():
        c = Counter( base for base, qual in reads )
        base, num_major = c.most_common(1)[0]
        num_all = sum(c.values())

        if num_major / num_all < 0.9:
            inconsis += 1
            continue

        if num_all == 1:
            if base in alt:
                if overlaped:
                    ooa += 1
                else:
                    ona += 1
            elif base in ref:
                if overlaped:
                    oor += 1
                else:
                    onr += 1
        else:
            if base in alt:
                if overlaped:
                    moa += 1
                else:
                    mna += 1
            elif base in ref:
                if overlaped:
                    mor += 1
                else:
                    mnr += 1

    for reads in single.values():
        c = Counter( base for base, qual in reads )
        base, num_major = c.most_common(1)[0]
        num_all = sum(c.values())

        if num_major / num_all < 0.9:
            inconsis += 1
            continue

        if num_all == 1:
            if base in alt:
                osa += 1
            elif base in ref:
                osr += 1
        else:
            if base in alt:
                msa += 1
            elif base in ref:
                msr += 1

    return mor, mnr, msr, oor, onr, osr, moa, mna, msa, ooa, ona, osa, inconsis
