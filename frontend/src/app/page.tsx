import Link from "next/link";


export default function Home() {
  return (
    <>
    <div className="flex flex-col p-10 md:p-20  w-full h-screen border-3 border-transparent
               [background:linear-gradient(#090d16,#090d16)_padding-box,linear-gradient(120deg,#ef4444,#ca8a04,#f97316)_border-box] 
               shadow-[0_0_15px_-3px_rgba(239,68,68,0.5)]">
      <div className="flex flex-col justify-around items-center">
        <span className="text-5xl  md:text-8xl ">😛</span>
        <p className="text-3xl md:text-8xl font-bold tracking-wide  bg-linear-120 from-red-500 via-yellow-600 to-orange-500 text-clip text-transparent bg-clip-text">Here to learn Auth ?</p>
        <p className="text-2xl md:text-4xl tracking-wider font-mono mt-5 md:mt-10 bg-linear-120 from-lime-400  to-white text-clip text-transparent bg-clip-text">Then let&apos;s dive in</p>
      </div>

      <div className="flex  flex-col justify-around items-center mt-10 md:mt-20 ">

        <Link href={"/login"} className="rounded-2xl border-2 border-transparent px-5 py-2 
               [background:linear-gradient(#090d16,#090d16)_padding-box,linear-gradient(120deg,#ef4444,#ca8a04,#f97316)_border-box] 
               shadow-[0_0_15px_-3px_rgba(239,68,68,0.5)]">
          <p className="font-bold text-2xl md:text-4xl bg-linear-120 from-red-600 via-yellow-600 to-orange-500 text-clip text-transparent bg-clip-text">Log in</p>
        </Link>

        <Link href={"/signup"}className="mt-5 md:mt-10 rounded-2xl border-2 border-transparent px-5 py-2 
               [background:linear-gradient(#090d16,#090d16)_padding-box,linear-gradient(120deg,#ef4444,#ca8a04,#f97316)_border-box] 
               shadow-[0_0_15px_-3px_rgba(239,68,68,0.5)]">
                <p className="font-bold text-2xl md:text-4xl bg-linear-120 from-green-500 via-yellow-600 to-orange-500 text-clip text-transparent bg-clip-text">Sign up</p>
          </Link>

      </div>
    </div>
    </>
  );
}
