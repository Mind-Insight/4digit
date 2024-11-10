import React from "react"
import JobSingle from "./JobSingle"
import './../styles/Job.css'

function Job() {
    return (
        <div className="Job">
            <h2 className="Job_title">Должности</h2>
            <div className="Job_main">
                <div className="Job_jobs">
                    <JobSingle name='Frontend-разработчик' />
                    <JobSingle name='UI/UX Дизайнер' />
                    <JobSingle name='QA-специалист' />
                    <JobSingle name='Backend-разработчик' />
                </div>
                <div className="control">
                    <div className="dot dot1 dot_active"></div>
                    <div className="dot dot2"></div>
                    <div className="dot dot3"></div>
                </div>
            </div>
        </div>
    )
}

export default Job