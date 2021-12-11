import Head from 'next/head'
import BarChart from '../components/BarChart'

export default function Home({trips_per_day}){
  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div>
        {/* Section 1 - Navbar */}
        {/* Section 2 - Top Cards */}
        <BarChart 
          datos_col = {trips_per_day["lista_viajes"]} 
          horas = {trips_per_day["lista_hora"]}
        />
        {/* Section 3 - Tables */}
      </div>
    </div>
  )
}

export const getStaticProps = async()=>{
  const {cardsData: trips_per_day} = await fetch("http://localhost:8888/cards/{trip_year}?a%C3%B1o=2021&mes=7&dia=18").then(d=>d.json())
  
  return {
    props:{
      trips_per_day
    }
  }
}