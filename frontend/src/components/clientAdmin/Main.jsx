import React from "react"
import '../../styles/clientAdmin/Main.css'
import date from '../../images/calendar.svg'
import arrow from '../../images/arrow.svg'
import Job from "./Job"
import Users from "./Users"
import Block from "./Block"
import GraphJobs from "./GraphJobs"

function Main() {
    return (
        <div className="Main">
            <div className="Main_title">
                <h2 className="Main_titleText">Привет, Никита!</h2>
                <div className="Main_titleDate">
                    <img src={date} alt="Calendar" className="Main_calendar" />
                    <p className="Main_textDate">8 нояб. - 16 нояб. 2024</p>
                    <img src={arrow} alt="Arrow" className="Main_arrow" />
                </div>
            </div>
            <div className="Main_Content">
                <div className="Main_left">
                    <Job className="JobComp" />
                    <Block className="BlockComp" />
                    <GraphJobs className="GraphJobsComp" />
                </div>
                <Users className="UsersComp" />
            </div>
        </div>
    )
}

export default Main