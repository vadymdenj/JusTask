import Nav from "./components/Nav"
import { Outlet } from "react-router-dom"
import { useSessionList, useUser } from "@clerk/clerk-react"
import { useNavigate } from "react-router-dom"

function App() {
  const { sessions } = useSessionList()
  const { user } = useUser()
  const navigate = useNavigate()
  // if (user && sessions?.length === 1) {
  //   navigate("/get-started")
  // }

  return (
    <div>
      <Nav />
      <Outlet />
    </div>
  )
}

export default App
