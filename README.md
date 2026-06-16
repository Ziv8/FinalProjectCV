# שאלה 1 — בעיית ספקים / צרכנים (תכנית לינארית)

קורס **אלגוריתמים מתקדמים למדמ״ח**, תשפ״ו — סמסטר אביב.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ziv8/FinalProjectCV/blob/main/suppliers_consumers.ipynb)

הפרויקט פותר את בעיית הספקים/צרכנים כתכנית לינארית (LP) ומחזיר את הכמות
הכוללת המקסימלית שמתקבלת אצל הצרכנים, יחד עם פתרון אופטימלי `F`.

## תוכן ה-Repo

| קובץ | תיאור |
|------|-------|
| [`suppliers_consumers.ipynb`](suppliers_consumers.ipynb) | מחברת Jupyter/Colab — הניסוח, הקוד, ההרצה והתוצאות |
| [`solution.py`](solution.py) | אותו פתרון כסקריפט פייתון רץ |
| `requirements.txt` | תלויות (PuLP) |

## הפעלה

**ב-Colab (מומלץ):** פותחים את `suppliers_consumers.ipynb` ולוחצים *Runtime → Run all*.

**מקומית:**
```bash
pip install -r requirements.txt
python solution.py
```

## ניסוח התכנית הלינארית

לכל קשת $(u_i, v_j) \in E$ משתנה $x_{ij} \ge 0$ — הכמות שהספק $u_i$ מספק לצרכן $v_j$.

$$\max \sum_{(u_i,v_j)\in E} x_{ij}$$

בכפוף ל:

$$\sum_{j:\,(u_i,v_j)\in E} x_{ij} \le a_i \quad (\text{קיבולת ספק}), \qquad
\sum_{i:\,(u_i,v_j)\in E} x_{ij} \le b_j \quad (\text{קיבולת צרכן}), \qquad
x_{ij} \ge 0$$

## פלט (קשתות איור 1)

```
Status: Optimal
כמות כוללת מקסימלית שמתקבלת אצל הצרכנים = 11.0

F (פתרון אופטימלי):
   ((u1, v1), 0.5)
   ((u1, v2), 1.5)
   ((u1, v4), 1.5)
   ((u2, v2), 1.5)
   ((u2, v5), 0.5)
   ((u3, v1), 2.0)
   ((u3, v3), 2.0)
   ((u4, v5), 1.5)
```

הערך 11.0 הוא ההיצע הכולל = הביקוש הכולל — כל הספקים וכל הצרכנים מנוצלים במלואם.

## שיחה עם ה-LLM

קישור לשיחה: <!-- הדביקו כאן את קישור השיתוף -->
