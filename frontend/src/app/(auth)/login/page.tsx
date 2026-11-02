

const LoginPage = () => {
  return (
    <div className="flex flex-col p-10 md:p-20  w-full h-screen border-3 border-transparent
               [background:linear-gradient(#090d16,#090d16)_padding-box,linear-gradient(120deg,#ef4444,#ca8a04,#f97316)_border-box] 
               shadow-[0_0_15px_-3px_rgba(239,68,68,0.5)]">

                <div className="flex justify-around items-center ">
                    <p className=" text-3xl md:text-8xl font-mono font-bold tracking-wide  bg-linear-120 from-red-500 via-yellow-600 to-orange-500 text-clip text-transparent bg-clip-text">Login Page</p>
                </div>


                <form action="" className="mt-20 md:mt-30 flex flex-col justify-around gap-5 md:gap-10  items-center">
                    <input type="email" name="email" placeholder="email" className="border p-2 md:p-2 px-4 md:px-6 rounded-2xl text-center md:text-2xl font-semibold"/>
                    <input type="password" name="password" placeholder="password" className="border p-2 md:p-2 px-4 md:px-6 rounded-2xl text-center md:text-2xl font-semibold"/>

                    <button type="submit"  className="border-2 p-2 px-5 rounded-2xl bg-linear-120 from-red-500 via-yellow-600 to-orange-500 border-transparent bg-clip-border font-extrabold md:text-2xl active:scale-110 ">login</button>
                </form>
                
    </div>
  )
}

export default LoginPage