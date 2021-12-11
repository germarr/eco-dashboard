import React from 'react';
import {Bar} from 'react-chartjs-2';
import Chart from 'chart.js/auto'


export default function BarChart({datos_col, horas}) {
    console.log(datos_col)
    return (
        <div className="px-6 py-6 rounded-t-sm">
          <h2 className="text-xs md:text-base font-semibold">Viajes por hora 🕔</h2>
          <Bar
            data={{
              labels: horas,
              datasets: [{
                label: '# de viajes',
                data: datos_col,
                backgroundColor: [
                  'rgba(255, 99, 132, 0.2)'
                ],
                borderColor: [
                  'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
              }]
            }}
            width={600}
            height={200}
            options={{
              maintainAspectRatio: true
            }}
          />
        </div>
    )
}
