function Validation(values){
    let error = {}
    const email_pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    const password_pattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,}$/

    if(values.name[0] === "") {
        error.name = "Name should not be empty"
    }
    else {
        error.name = ""
    }

    if(values.email[0] === ""){
        error.email = "Email should not be empty"
    }
    else if(!email_pattern.test(values.email[0])) {
        error.email = "Email should only be alphanumeric characters"
    } else {
        error.email = ""
    }

    if(values.password[0] === "") {
        error.password = "Password should not be empty"
    }
    else if(!password_pattern.test(values.password[0])) {
        error.password = "Password should contain at least one Uppercase letter one lowercase letter and a number. No special characters."
    } else {
        error.password = ""
    }
    return error;
}

export default Validation;