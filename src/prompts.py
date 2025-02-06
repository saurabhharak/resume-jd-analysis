RESUME_EXTRACTION_PROMPT = """
You are provided with a candidate's resume. 
Your task is to extract only the relevant information from the text while ensuring that all extracted details are standardized and properly formatted.

'Standardization Rules:
- Convert all job titles, skills, and other attributes into their full, properly capitalized form (e.g., "ML Engineer" → "Machine Learning Engineer").
- Ensure no abbreviations are used in the extracted output.
- If an attribute's value is missing or unavailable, return null.

'Extract the following details:
- Candidate Name: Full name of the candidate.
- Job Title: Standardized job title.
- Skills: List of skills in a standardized format.
- Years of Experience: Total years of relevant experience.
- Certifications: List of relevant certifications.
- Education: Highest degree obtained and the institution name.
- Other: Any additional relevant information.

''Candidate Resume:
{resume_text}

''Output Format:
{format_instructions}
"""

JD_EXTRACTION_PROMPT = """
You are provided with a job description.
Your task is to extract only the relevant information while ensuring that all extracted details are standardized and properly formatted.

' Standardization Rules:
- Convert all job titles, skills, and other attributes into their full, properly capitalized form (e.g., "Data Engr" → "Data Engineer").
- Ensure no abbreviations are used in the extracted output.
- If an attribute's value is missing or unavailable, return null.

' Extract the following details:
- Job Title: Standardized job title.
- Skills: List of required skills in a standardized format.
- Years of Experience: Minimum required years of experience.
- Certifications: List of required certifications (if mentioned).
- Education: Minimum required degree and field of study.
- Other: Any additional relevant requirements.

''Job Description:
{job_description}

''Output Format:
{format_instructions}
"""

MATCH_ANALYSIS_PROMPT = """
You are an AI assistant specialized in evaluating candidate resumes against job descriptions (JD). Your task is to analyze how well a candidate's profile aligns with a given job description based on specific criteria.
 
### **Scoring Guidelines:**
To evaluate the resumes against the Job Description, use the following scoring breakdown:
- **Match on Skills (40%)**: How well the candidate's skills align with the JD.
- **Match on Experience (30%)**: Relevance and duration of the candidate's experience.
- **Match on Certifications & Education (20%)**: Certifications, degrees, or other qualifications.
- **Other Factors (10%)**: Additional relevant elements, such as soft skills, location, or languages.
 
Each resume should receive a total score out of 100 based on these criteria.
 
### **Scoring Criteria:**
1. **Skills Matching** (40 Points)
   - Compare the candidate's listed skills with the JD's required skills.
   - Match exact skills and award points proportionally.
   - If a skill is partially met (e.g., general ML knowledge but missing specific frameworks like TensorFlow), note it.
   - Highlight missing skills that significantly impact the match.
   - **Categorization:**
     - Essential: Must-have skills for the role.
     - Preferred: Beneficial but not required.
     - Bonus: Extra skills that add value.
   - **Match Symbols:**
     - ✅ = Exact match
     - 🟡 = Partial match (transferable skills)
     - ❌ = No match
2. **Experience Matching** (30 Points)
   - Compare the candidate's years of experience with the JD requirement.
   - If the candidate meets or exceeds the experience, assign full points.
   - If underqualified, assign points proportionally.
 
3. **Certifications & Education Matching** (20 Points)
   - Compare candidate certifications and degrees with JD requirements.
   - If certifications are not required but relevant, assign bonus points.
   - If required certifications are missing, reduce points.
   - **Clarification:** Certifications contribute to validation of skills but are not always mandatory.
 
4. **Other Relevant Factors** (10 Points - Qualitative Evaluation)
   - Check for any additional requirements (e.g., soft skills, location, language proficiency, domain knowledge, tools).
   - Assign qualitative rating:
     - ✅ Fully Met
     - 🟡 Partially Met
     - ❌ Not Met
   - **Impact:** If unmet, specify how it affects role readiness.
 
---
 
### **Task Instructions:**
- Analyze the candidate's **resume information** and compare it with the **job description**.
- Assign a **match percentage** based on the scoring criteria.
- Provide a structured breakdown explaining **why the score was assigned**.
- Clearly highlight **mismatches** and **suggest areas for improvement**.
- Ensure the extracted details are standardized (e.g., "ML Engineer" → "Machine Learning Engineer").
- Return structured output in the required format.
 
---
 
### **Candidate Resume Details:**
{resume_details}
 
### **Job Description Details:**
{job_description_details}
 
---
 
### **Output Format Example:**
```
Final Match Score: **XX.XX%** (Indicates how well the candidate fits the JD)
 
### **Analysis Breakdown:**
1. **Job Title Match**
   - Candidate's Job Title: [Extracted Title]
   - JD Job Title: [Extracted JD Title]
   - **Impact:** [Does it match? Partially match? If not, why?]
 
2. **Skills Comparison**:

→ Python → Candidate's Skill: Python → ✅ Match
→ SQL → Candidate's Skill: SQL → ✅ Match
→ Machine Learning Tools → Candidate's Skill: ML (but no TensorFlow/PyTorch) → 🟡 Partial
→ Cloud Platforms → Candidate's Skill: Not listed → ❌ No Match
→ Airflow → Candidate's Skill: Not listed → ❌ No Match
 
- **Impact:** Highlight missing skills that reduce the score.
3. **Experience Years**
   - JD Requirement: [X years]
   - Candidate Experience: [Y years]
   - **Impact:** Does the candidate meet/exceed requirements?
 
4. **Certifications**
   - JD Certifications Required: [List]
   - Candidate Certifications: [List]
   - **Impact:** Does the candidate have relevant certifications?
 
5. **Education**
   - JD Required Education: [CS, Engineering, etc.]
   - Candidate's Education: [Extracted Degree]
   - **Impact:** Is the education relevant?
 
6. **Other Requirements**
   - JD requires experience in LLMs, Prompt Engineering, OpenAI, etc.
   - Candidate lacks [Missing aspects].
   - **Impact:** If critical to the role, explain how it affects the score.
 
1. **Skills Matching (40%)**
   - Score: X/40
   - ✅/🟡/❌ (Match level)
   - Impact: Explanation of strengths and gaps
 
2. **Experience Matching (30%)**
   - Score: X/30
   - ✅/🟡/❌ (Match level)
   - Impact: Explanation of relevance
 
3. **Certifications & Education (20%)**
   - Score: X/20
   - ✅/🟡/❌ (Match level)
   - Impact: Explanation of importance
 
4. **Other Factors (10%)**
   - Score: X/10
   - ✅/🟡/❌ (Match level)
   - Impact: Explanation of additional strengths/gaps
 
---
 
### **Final Analysis Summary:**

→ Skills → Score: X/40 → Match Level: ✅/🟡/❌ (Match/Partial/No)

→ Experience Years → Score: X/30 → Match Level: ✅ (Good) / ❌ (Low)

→ Certifications & Education → Score: X/20 → Match Level: ✅ (Relevant) / ❌ (Not needed)

→ Other Factors → Score: X/10 → Match Level: ✅ (Met) / ❌ (Not Met)
 
➡ **Final Match Score: XX.XX%**
➡ **Fit Category:**
   - 0-50% = Poor Fit
   - 51-75% = Medium Fit
   - 76-100% = Strong Fit
 
---
 
### **Conclusion & Recommendations**
- Based on the match score, summarize whether the candidate is a good fit.
- Suggest areas where they can improve to increase their match score.
- Provide specific recommendations (e.g., learning specific tools, gaining experience in a certain domain).
- Ensure the explanation logically justifies the score.
```
 
---
 
**Important Notes:**
- The output must be structured and detailed in MD format.
- Highlight mismatches logically.
- Ensure the analysis follows the outlined scoring method.
 
Start your analysis now!
"""
