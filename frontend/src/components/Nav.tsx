import { useUser, SignInButton } from "@clerk/clerk-react"

export default function Nav() {
  const { user } = useUser()

  return (
    <header className="flex items-center justify-between px-9 py-3 bg-gray-400">
      <h1 className="font-display text-2xl flex flex-col justify-center items-center w-fit text-zinc-100">
        Turbo <span>Tax</span>
      </h1>
      {!user ? (
        <SignInButton mode="modal">Login</SignInButton>
      ) : (
        <div>
          <img src={user.imageUrl} alt="" />
        </div>
      )}
    </header>
  )
}
