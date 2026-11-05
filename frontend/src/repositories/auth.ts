"use server";


type UserInput = {
    name: string;
    email: string;
    password: string;
}

export async function SignupUser(Props: UserInput) {

    const response  = await fetch("http://127.0.0.1:8000/signup",
        {
            method: "POST",
            headers: {
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                name: Props.name,
                email: Props.email,
                password: Props.password
            })
        }
    )

    const data = await response.json();

    if (response.status != 200 ) {
        return {
            detail: data.detail
        }
    };

    return data

}