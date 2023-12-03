import CreateTask from "../components/CreateTask"
import { useUser } from "@clerk/clerk-react"
export default function Home() {
  const { user } = useUser()

  if (!user) return <div>most be logged in to view this page</div>
  const calendar = [
    {
      name: "Work",
      from: "6:30am",
      to: "4:30pm",
    },
    {
      name: "Gym",
      from: "5:00pm",
      to: "6:30pm",
    },

    {
      name: "Dinner",
      from: "7:00pm",
      to: "8:00pm",
    },
  ]
  return (
    <div className="flex justify-around pt-12">
      <div className="w-full max-w-xs flex gap-4 flex-col">
        {calendar.map((item) => (
          <div className="w-full max-w-xs bg-slate-400 px-4 py-2 rounded-lg">
            <div className="text-lg font-medium">{item.name}</div>
            <div>
              {item.from}-{item.to}
            </div>
          </div>
        ))}
      </div>
      <CreateTask />
    </div>
  )
}
