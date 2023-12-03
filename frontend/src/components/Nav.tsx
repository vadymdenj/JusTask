import { useUser, SignInButton, SignOutButton } from "@clerk/clerk-react"
import logoRoute from "../assets/logo.svg"

export default function Nav() {
  const { user } = useUser()

  return (
    <header className="flex items-center justify-between px-9 py-3 bg-gray-400">
      <h1 className="font-display text-2xl flex flex-col justify-center items-center w-fit text-zinc-100">
        <img src={logoRoute} alt="" width={40} height={40} />
      </h1>
      {!user ? (
        <div>
          <SignInButton mode="modal" afterSignInUrl="/get-started">
            Login
          </SignInButton>
        </div>
      ) : (
        <div className="flex gap-4">
          <SignOutButton>Sign out</SignOutButton>
          <img
            src={user.imageUrl}
            width={40}
            height={40}
            className="rounded-full"
          />
        </div>
      )}
    </header>
  )
}
