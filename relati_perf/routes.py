from relati_perf.directions import *

RELATI_NORMAL_ROUTES = [
    [F],
    [B],
    [L],
    [R],

    [FL],
    [FR],
    [BL],
    [BR],
]

RELATI_REMOTE_ROUTES = [
    [FF, F],
    [BB, B],
    [LL, L],
    [RR, R],

    [FFLL, FL],
    [FFRR, FR],
    [BBLL, BL],
    [BBRR, BR],
]

RELATI_REMOTE_STABLE_ROUTES = [
    [FFL, FF, F],
    [FFR, FF, F],
    [BBL, BB, B],
    [BBR, BB, B],

    [FFL, FL, F],
    [FFR, FR, F],
    [BBL, BL, B],
    [BBR, BR, B],

    [FFL, FL, L],
    [FFR, FR, R],
    [BBL, BL, L],
    [BBR, BR, R],

    [FLL, FL, F],
    [FRR, FR, F],
    [BLL, BL, B],
    [BRR, BR, B],

    [FLL, FL, L],
    [FRR, FR, R],
    [BLL, BL, L],
    [BRR, BR, R],

    [FLL, LL, L],
    [FRR, RR, R],
    [BLL, LL, L],
    [BRR, RR, R],
]

RELATI_ROUTES = [
    *RELATI_NORMAL_ROUTES,
    *RELATI_REMOTE_ROUTES,
    *RELATI_REMOTE_STABLE_ROUTES,
]
