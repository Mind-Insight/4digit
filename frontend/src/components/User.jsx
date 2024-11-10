import { useState } from 'react'
import React from "react"
import Arrow from './../images/arrow.svg'
import './../styles/Users.css'
import UserProp from './UserProp'

function User(props) {
    const [isExpanded, setIsExpanded] = useState(false);

    const handleToggle = () => {
        setIsExpanded(!isExpanded);
    };

    return (
        <div className="User">
            <div className="User_main">
                <div className="User_photoBlock">
                    <img src={props.photo} alt="user_photo" className="User_photo" />
                </div>
                <div className="User_nameBlock">
                    <p className="User_name">{props.name}</p>
                    <p className="User_age">{props.age}</p>
                </div>
                <p className="User_phone">{props.phone}</p>
                <p className="User_email">{props.email}</p>
                <div className="User_softBlock">
                    <p className="User_soft">{(+props.soft + +props.hard) / 2}%</p>
                </div>
                <img src={Arrow} alt="arrow" className={`User_button ${isExpanded ? 'rotated' : ''}`} onClick={handleToggle} />
            </div>

            {
                isExpanded && (
                    <UserProp onDelete={() => props.onDelete(props.id)} className='UserProp' soft={props.soft} video={props.video} type={props.type} hard={props.hard}/>
                )
            }

        </div>


    )
}

export default User