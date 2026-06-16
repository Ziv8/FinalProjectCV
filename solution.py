# -*- coding: utf-8 -*-
"""
שאלה 1 — בעיית ספקים/צרכנים (Suppliers / Consumers)
פתרון התכנית הלינארית באמצעות PuLP.

הרעיון: לכל קשת (u_i, v_j) בגרף הדו-צדדי מגדירים משתנה x_ij >= 0,
הכמות שהספק u_i מספק לצרכן v_j. ממקסמים את סך הכמות שמתקבלת אצל הצרכנים,
תחת אילוצי הקיבולת של הספקים (a_i) ושל הצרכנים (b_j).
"""

import pulp

# ---------------------------------------------------------------------------
# נתונים מתוך איור 1
# ---------------------------------------------------------------------------

# קיבולת ספקים: כמה כל ספק יכול לספק לכל היותר (a_i)
a = {"u1": 3.5, "u2": 2.0, "u3": 4.0, "u4": 1.5}

# קיבולת צרכנים: כמה כל צרכן יכול לצרוך לכל היותר (b_j)
b = {"v1": 2.5, "v2": 3.0, "v3": 2.0, "v4": 1.5, "v5": 2.0}

# קשתות הגרף הדו-צדדי E: הזוג (u, v) קיים אם הספק u יכול לספק לצרכן v.
# ⚠️ חשוב: השלימו/וודאו שהרשימה תואמת *בדיוק* לאיור 1 שלכם.
#    הקשתות שלמטה הן אלו שמופיעות בדוגמה בשאלה (u2 מחובר רק ל-v2 ו-v5).
edges = [
    ("u1", "v1"), ("u1", "v2"), ("u1", "v4"),
    ("u2", "v2"), ("u2", "v5"),                    # u2 מחובר רק ל-v2, v5
    ("u3", "v1"), ("u3", "v3"), ("u3", "v4"),
    ("u4", "v2"), ("u4", "v3"), ("u4", "v5"),
]

# ---------------------------------------------------------------------------
# בניית התכנית הלינארית ופתרונה
# ---------------------------------------------------------------------------

def solve(a, b, edges, verbose=True):
    prob = pulp.LpProblem("Suppliers_Consumers", pulp.LpMaximize)

    # משתני החלטה: x[(u, v)] >= 0  עבור כל קשת
    x = {(u, v): pulp.LpVariable(f"x_{u}_{v}", lowBound=0) for (u, v) in edges}

    # פונקציית מטרה: מקסום סך הכמות שהצרכנים מקבלים
    prob += pulp.lpSum(x.values()), "Total_delivered"

    # אילוץ קיבולת לכל ספק: סכום היציאות שלו <= a_u
    for u in a:
        prob += pulp.lpSum(x[(uu, v)] for (uu, v) in edges if uu == u) <= a[u], f"supply_{u}"

    # אילוץ קיבולת לכל צרכן: סכום הכניסות אליו <= b_v
    for v in b:
        prob += pulp.lpSum(x[(u, vv)] for (u, vv) in edges if vv == v) <= b[v], f"demand_{v}"

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if verbose:
        print("Status:", pulp.LpStatus[prob.status])
        print(f"כמות כוללת מקסימלית שמתקבלת אצל הצרכנים = {pulp.value(prob.objective)}")
        print("\nF (פתרון אופטימלי) — רק קשתות עם כמות חיובית:")
        for (u, v) in edges:
            val = x[(u, v)].value()
            if val and val > 1e-9:
                print(f"   (({u}, {v}), {round(val, 4)})")

        print("\nניצול קיבולת הספקים:")
        for u in a:
            used = sum(x[(uu, v)].value() for (uu, v) in edges if uu == u)
            print(f"   {u}: {round(used, 4)} / {a[u]}")

        print("ניצול קיבולת הצרכנים:")
        for v in b:
            used = sum(x[(u, vv)].value() for (u, vv) in edges if vv == v)
            print(f"   {v}: {round(used, 4)} / {b[v]}")

    return prob, x


if __name__ == "__main__":
    solve(a, b, edges)
