import { useState } from "react"
import { useForm, SubmitHandler } from "react-hook-form"
import Places from "../components/Places"
import { Link } from "react-router-dom"

export default function GetStarted() {
  const [tasks, setTasks] = useState<{ fixed: Task[]; free: Task[] }>({
    fixed: [],
    free: [],
  })

  function handleAddTask(task: Task) {
    if (task.type === "fixed-task") {
      setTasks((prev) => ({
        free: [...prev.free],
        fixed: [...prev.fixed, task],
      }))
    } else {
      setTasks((prev) => ({
        fixed: [...prev.fixed],
        free: [...prev.free, task],
      }))
    }
  }
  return (
    <div className="flex flex-col pt-20 gap-8">
      <div className="m-auto flex items-center flex-col">
        <h1 className="font-display text-5xl m-auto">Welcome!</h1>
        <p className="m-auto text-xl">
          Let's get started with your first agenda...
        </p>
      </div>

      <div className="flex justify-between w-full max-w-7xl m-auto">
        <div className="w-full max-w-sm">
          <p className="py-2 px-4 rounded-t-lg font-bold text-lg w-full text-gray-100 bg-blue-500">
            <span className="underline font-bold">Fixed</span> tasks
          </p>
          {tasks.fixed.map((t) => (
            <div>{t.name}</div>
          ))}
        </div>
        <div className="w-full max-w-sm">
          <p className="py-2 px-4 rounded-t-lg font-bold text-lg w-full text-gray-100 bg-blue-500">
            <span className="underline font-bold">Free</span> tasks
          </p>
          {tasks.free.map((t) => (
            <div>{t.name}</div>
          ))}
        </div>
        <Form handleAddTask={handleAddTask} />
      </div>

      <Link to="/">Create agenda</Link>
    </div>
  )
}

type EventType = "fixed-task" | "free-task"
type DurationUnit = "hours" | "minutes"

type Task = {
  name: string
  address: string
  type: EventType
  from: string
  to: string
  duration: {
    value: number
    unit: DurationUnit
  }
}

function Form({ handleAddTask }: { handleAddTask: (task: Task) => void }) {
  const { register, handleSubmit, watch, reset } = useForm<Task>({
    defaultValues: {
      type: "fixed-task",
    },
  })

  const onSubmit: SubmitHandler<Task> = (data) => {
    handleAddTask(data)
    reset()
  }
  return (
    <div className="flex flex-col w-full max-w-sm">
      <p className="bg-blue-500 py-2 px-4 rounded-t-lg text-xl text-gray-100 font-bold">
        Add Task
      </p>
      <form
        onSubmit={handleSubmit(onSubmit)}
        className="flex flex-col border-2 py-2 px-4 border-blue-500 rounded-b-lg gap-4"
      >
        <label className="flex flex-col gap-2">
          <span className="capitalize">Name</span>
          <input
            type="text"
            className="rounded-lg"
            required
            {...register("name")}
          />
        </label>
        <label className="flex flex-col gap-2">
          <span className="capitalize">Address</span>
          <Places>
            <input
              type="text"
              className="rounded-lg w-full form-control"
              required
              {...register("address")}
              placeholder="Enter a location"
            />
          </Places>
        </label>
        <label className="flex flex-col gap-2">
          <span> Event Type</span>
          <select id="" className="rounded-lg" required {...register("type")}>
            <option value="fixed-task">Fixed Event</option>
            <option value="free-task">Free Task</option>
          </select>
        </label>
        <label htmlFor="" className="flex flex-col gap-2">
          <span>Duration</span>

          {watch().type === "fixed-task" ? (
            <div className="flex gap-4">
              <label htmlFor="" className="flex gap-2 items-center">
                <span>From</span>
                <input
                  {...register("from")}
                  type="time"
                  name=""
                  id=""
                  className="rounded-lg"
                  required
                />
              </label>
              <label htmlFor="" className="flex gap-2 items-center">
                <span>To</span>
                <input
                  type="time"
                  {...register("to")}
                  className="rounded-lg"
                  required
                />
              </label>
            </div>
          ) : (
            <div className="flex">
              <input
                {...register("duration.value")}
                type="number"
                className="rounded-l-lg"
                min={0}
                required
              />
              <select
                id=""
                className="rounded-r-lg"
                {...register("duration.unit")}
                required
              >
                <option value="hours">Hours</option>
                <option value="minutes">Minutes</option>
              </select>
            </div>
          )}
        </label>

        <button className="py-2 px-6 bg-blue-500 hover:bg-blue-600 transition-colors w-fit text-gray-100 font-bold m-auto rounded-lg">
          Add
        </button>
      </form>
    </div>
  )
}
