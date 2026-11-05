

const LoginForm = () => {
  return (
    <div>
        <form action="" className="mt-20 md:mt-30 flex flex-col justify-around gap-5 md:gap-10  items-center">
            <input type="email" name="email" placeholder="email" className="border p-2 md:p-2 px-4 md:px-6 rounded-2xl text-center md:text-2xl font-semibold"/>
            <input type="password" name="password" placeholder="password" className="border p-2 md:p-2 px-4 md:px-6 rounded-2xl text-center md:text-2xl font-semibold"/>

            <button type="submit"  className="border-2 p-2 px-5 rounded-2xl bg-linear-120 from-red-500 via-yellow-600 to-orange-500 border-transparent bg-clip-border font-extrabold md:text-2xl active:scale-110 ">login</button>
        </form>
    </div>
  )
}

export default LoginForm