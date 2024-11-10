import React from "react"
import Arrow from '../../images/arrow.svg'
import '../../styles/clientAdmin/Users.css'

function User(props) {
    return (
        <div className="User">
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
                <p className="User_soft">{props.soft}%</p>
            </div>
            <img src={Arrow} alt="arrow" className="User_button" />
        </div>
    )
}

export default User