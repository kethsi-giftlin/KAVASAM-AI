from fastapi import APIRouter, Depends, HTTPException
from app.schemas import *
from app.db import get_conn
from app.security import hash_password, verify_password, make_token
from app.auth import current_user
from app.services.analyzer import analyze_text, analyze_url
from app.services.chatbot import answer
from app.services.learning import LESSONS, QUIZ

router=APIRouter()

def uid(u): return int(u["sub"])

@router.post("/auth/register")
def register(r:RegisterRequest):
    conn=get_conn()
    if conn.execute("SELECT id FROM users WHERE email=?",(r.email.lower(),)).fetchone(): conn.close(); raise HTTPException(400,"Email already registered")
    cur=conn.execute("INSERT INTO users(name,email,password_hash) VALUES(?,?,?)",(r.name.strip(),r.email.lower(),hash_password(r.password)))
    conn.commit(); user_id=cur.lastrowid; conn.close()
    return {"token":make_token(user_id,r.email.lower()),"user":{"id":user_id,"name":r.name.strip(),"email":r.email.lower()}}

@router.post("/auth/login")
def login(r:LoginRequest):
    conn=get_conn(); row=conn.execute("SELECT * FROM users WHERE email=?",(r.email.lower(),)).fetchone(); conn.close()
    if not row or not verify_password(r.password,row["password_hash"]): raise HTTPException(401,"Invalid email or password")
    return {"token":make_token(row["id"],row["email"]),"user":{"id":row["id"],"name":row["name"],"email":row["email"]}}

@router.get("/me")
def me(u=Depends(current_user)):
    conn=get_conn(); row=conn.execute("SELECT id,name,email FROM users WHERE id=?",(uid(u),)).fetchone(); conn.close(); return dict(row)

@router.post("/analyze/text")
def text(r:TextRequest,u=Depends(current_user)):
    result=analyze_text(r.text); conn=get_conn(); conn.execute("INSERT INTO analyses(user_id,kind,input_preview,risk_score,risk_level,threat_type) VALUES(?,?,?,?,?,?)",(uid(u),"text",r.text[:180],result["risk_score"],result["risk_level"],result["threat_type"])); conn.commit(); conn.close(); return result

@router.post("/analyze/url")
def url(r:URLRequest,u=Depends(current_user)):
    result=analyze_url(r.url); conn=get_conn(); conn.execute("INSERT INTO analyses(user_id,kind,input_preview,risk_score,risk_level,threat_type) VALUES(?,?,?,?,?,?)",(uid(u),"url",r.url[:180],result["risk_score"],result["risk_level"],"URL RISK")); conn.commit(); conn.close(); return result

@router.get("/history")
def history(u=Depends(current_user)):
    conn=get_conn(); rows=conn.execute("SELECT * FROM analyses WHERE user_id=? ORDER BY id DESC LIMIT 30",(uid(u),)).fetchall(); conn.close(); return {"items":[dict(x) for x in rows]}

@router.get("/dashboard")
def dashboard(u=Depends(current_user)):
    conn=get_conn(); user=conn.execute("SELECT name FROM users WHERE id=?",(uid(u),)).fetchone(); analyses=conn.execute("SELECT COUNT(*) c, SUM(CASE WHEN risk_score>=61 THEN 1 ELSE 0 END) danger FROM analyses WHERE user_id=?",(uid(u),)).fetchone(); lessons=conn.execute("SELECT COUNT(*) c FROM lesson_progress WHERE user_id=?",(uid(u),)).fetchone(); quizzes=conn.execute("SELECT COUNT(*) c, SUM(correct) good FROM quiz_attempts WHERE user_id=?",(uid(u),)).fetchone(); conn.close()
    checked=analyses["c"] or 0; danger=analyses["danger"] or 0; lc=lessons["c"] or 0; qc=quizzes["c"] or 0; good=quizzes["good"] or 0
    score=min(100,70+min(15,lc*3)+min(10,good*2)-min(15,danger*2))
    return {"name":user["name"],"overall_score":score,"threats_checked":checked,"potential_threats":danger,"lessons_completed":lc,"lessons_total":len(LESSONS),"quiz_accuracy":round((good/qc)*100) if qc else 0,"recommendation":"Improve Social Engineering Awareness" if lc<3 else "Keep practicing with scenario-based quizzes"}

@router.get("/lessons")
def lessons(): return {"lessons":LESSONS}

@router.post("/lessons/complete")
def lesson_complete(r:LessonRequest,u=Depends(current_user)):
    if r.lesson_id not in [x["id"] for x in LESSONS]: raise HTTPException(404,"Lesson not found")
    conn=get_conn(); conn.execute("INSERT OR IGNORE INTO lesson_progress(user_id,lesson_id) VALUES(?,?)",(uid(u),r.lesson_id)); conn.commit(); conn.close(); return {"success":True}

@router.get("/quiz")
def quiz(): return {k:v for k,v in QUIZ.items() if k!="correct"}

@router.post("/quiz/submit")
def quiz_submit(r:QuizRequest,u=Depends(current_user)):
    correct=r.answer.strip().upper()==QUIZ["correct"]; conn=get_conn(); conn.execute("INSERT INTO quiz_attempts(user_id,correct) VALUES(?,?)",(uid(u),1 if correct else 0)); conn.commit(); conn.close(); return {"correct":correct,"score":100 if correct else 0,"feedback":"Correct. Verify unexpected requests through a trusted channel." if correct else "Not quite. Pause and independently verify unexpected requests."}

@router.post("/chat")
def chat(r:ChatRequest,u=Depends(current_user)): return answer(r.message)
