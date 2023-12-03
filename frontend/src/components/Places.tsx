import { useRef } from "react"
import {
  StandaloneSearchBox,
  useJsApiLoader,
  type Libraries,
} from "@react-google-maps/api"

const libraries: Libraries = ["places"]

export default function Places({ children }: { children: React.ReactNode }) {
  const inputRef = useRef<HTMLInputElement | null>()
  const { isLoaded, loadError } = useJsApiLoader({
    googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAP_KEY,
    libraries,
  })

  const handlePlaceChanged = () => {
    if (!inputRef.current) return

    const [place] = inputRef.current.getPlaces()
    if (place) {
      console.log(place.formatted_address)
      console.log(place.geometry.location.lat())
      console.log(place.geometry.location.lng())
    }
  }

  return (
    isLoaded && (
      <StandaloneSearchBox
        onLoad={(ref) => (inputRef.current = ref)}
        onPlacesChanged={handlePlaceChanged}
      >
        {children}
      </StandaloneSearchBox>
    )
  )
}
