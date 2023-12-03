// import Places from "./Places"

export default function CreateTask() {
  return (
    <div className="flex flex-col w-full max-w-sm">
      <p className="bg-blue-500 py-2 px-4 rounded-t-lg text-xl text-gray-100 font-bold">
        Add Task
      </p>
      <form
        action=""
        className="flex flex-col border-2 py-2 px-4 border-blue-500 rounded-b-lg gap-4"
      >
        <Input name="name" />
        <Input name="address" />

        <label className="gap-2">
          <span>Duration</span>
          <div className="flex">
            <input type="number" className="rounded-l-lg" min={0} />
            <select name="durationUnit" id="" className="rounded-r-lg">
              <option value="hours">Hours</option>
              <option value="minutes">Minutes</option>
            </select>
          </div>
        </label>
        <button className="py-2 px-6 bg-blue-500 hover:bg-blue-600 transition-colors w-fit text-gray-100 font-bold m-auto rounded-lg">
          Create
        </button>
      </form>
    </div>
  )
}

export function Input({ name }: { name: string }) {
  return (
    <label className="flex flex-col gap-2">
      <span className="capitalize">{name}</span>
      <input type="text" className="rounded-lg" required />
    </label>
  )
}
