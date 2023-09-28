import axios from 'axios';
import React, { useState } from "react";
import { Link } from "react-router-dom";

function Signup() {
  const [values, setValues] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [errors, setErrors] = useState({});

  const handleInput = (event) => {
    setValues({ ...values, [event.target.name]: event.target.value });

    // Clear the error message when the user starts typing
    setErrors({ ...errors, [event.target.name]: "" });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Perform validation
    const validationErrors = {};

    if (values.name.trim() === "") {
      validationErrors.name = "Name is required";
    }

    if (values.email.trim() === "") {
      validationErrors.email = "Email is required";
    }

    if (values.password.trim() === "") {
      validationErrors.password = "Password is required";
    }

    // You can add more complex validation if needed, such as email format, password strength, etc.

    // If there are errors, update the state with the validation errors
    if (Object.keys(validationErrors).length > 0) {
        setErrors(validationErrors);
      } else {
        try {
          const response = await axios.post(
            '/apiRegisterUser',
            JSON.stringify(values), // Convert values to JSON string
            {
              headers: {
                'Content-Type': 'application/json', // Set the Content-Type header to application/json
              },
            }
          );
          console.log(response.data.message);
          window.location.href = '/chat';
          alert(response.data.message);
          // Handle successful registration (e.g., redirect to login page)
        } catch (error) {
          console.log(error.response.data.error);
          alert(error.response.data.error);
          // Handle registration error (e.g., display error message)
        }
      }
    };

  return (
    <div className="formBox">
      <div className="bg-white p-3 rounded w-25">
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="name">
              <strong>Name</strong>
            </label>
            <input
              type="text"
              placeholder="Enter Name"
              name="name"
              value={values.name}
              onChange={handleInput}
              className="form-control rounded-0"
            />
            {errors.name && <span className="text-danger">{errors.name}</span>}
          </div>
          <div className="mb-3">
            <label htmlFor="email">
              <strong>Email</strong>
            </label>
            <input
              type="email"
              placeholder="Enter Email"
              name="email"
              value={values.email}
              onChange={handleInput}
              className="form-control rounded-0"
            />
            {errors.email && (
              <span className="text-danger">{errors.email}</span>
            )}
          </div>
          <div className="mb-3">
            <label htmlFor="password">
              <strong>Password</strong>
            </label>
            <input
              type="password"
              placeholder="Enter Password"
              name="password"
              value={values.password}
              onChange={handleInput}
              className="form-control rounded-0"
            />
            {errors.password && (
              <span className="text-danger">{errors.password}</span>
            )}
          </div>
          <button
            type="submit"
            className="btn btn-success w-100 rounded-0"
          >
            Sign Up
          </button>
          <Link
            to="/"
            className="btn btn-default border w-100 bg-light rounded-0 text-decoration-none"
          >
            Log In
          </Link>
        </form>
      </div>
    </div>
  );
}

export default Signup;
