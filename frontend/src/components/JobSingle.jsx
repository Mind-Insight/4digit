import React from "react";
import arrow from "./../images/top_arrow.svg"
import './../styles/Job.css'

function Job_single(props) {
    return (
        <div className="Job_single">
            <p className="Job_name">{props.name}</p>
            <div className="Job_btn">
                <img src={arrow} alt="click" />
            </div>
        </div>
    )
}

export default Job_single