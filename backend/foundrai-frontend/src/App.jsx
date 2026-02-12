import { useState } from "react"

function App() {
  const [form, setForm] = useState({
    problem: "",
    target_audience: "",
    revenue_model: "",
    industry: "",
    region: ""
  })

  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)

    try {
      const response = await fetch("http://127.0.0.1:8000/idea/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(form)
      })

      const data = await response.json()
      setResult(data)
    } catch (error) {
      console.error("Error:", error)
    }

    setLoading(false)
  }

  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center">
      <div className="w-full max-w-lg bg-gray-950 p-8 rounded-2xl shadow-2xl">

        <h1 className="text-3xl font-bold text-green-400 mb-8 text-center">
          FoundrAI 🚀
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">

          <input
            name="problem"
            placeholder="Problem"
            value={form.problem}
            onChange={handleChange}
            required
            className="w-full p-3 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          />

          <input
            name="target_audience"
            placeholder="Target Audience"
            value={form.target_audience}
            onChange={handleChange}
            required
            className="w-full p-3 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          />

          <input
            name="revenue_model"
            placeholder="Revenue Model"
            value={form.revenue_model}
            onChange={handleChange}
            required
            className="w-full p-3 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          />

          <input
            name="industry"
            placeholder="Industry"
            value={form.industry}
            onChange={handleChange}
            required
            className="w-full p-3 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          />

          <input
            name="region"
            placeholder="Region"
            value={form.region}
            onChange={handleChange}
            required
            className="w-full p-3 bg-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
          />

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-green-500 py-3 rounded-lg font-semibold hover:bg-green-600 transition disabled:opacity-50"
          >
            {loading ? "Analyzing..." : "Analyze Idea"}
          </button>

        </form>

        {result && (
          <div className="mt-8 bg-gray-900 p-6 rounded-xl">

            <h2 className="text-xl font-bold text-green-300 mb-4 text-center">
              Results
            </h2>

            <p className="mb-2">
              <span className="font-semibold">Final Score:</span> {result.final_score}
            </p>

            <p className="mb-2">
              <span className="font-semibold">Risk Level:</span> {result.risk_level}
            </p>

            {result.analysis && (
              <p className="text-gray-300 mt-4">
                {result.analysis}
              </p>
            )}

            {/* ✅ EXISTING STARTUPS SECTION */}
            {result.similar_startups && result.similar_startups.length > 0 && (
              <div className="mt-6">
                <h3 className="text-green-400 font-semibold mb-2">
                  Similar Existing Startups
                </h3>

                <ul className="list-disc list-inside text-gray-300 space-y-1">
                  {result.similar_startups.map((startup, index) => (
                    <li key={index}>{startup}</li>
                  ))}
                </ul>
              </div>
            )}

          </div>
        )}

      </div>
    </div>
  )
}

export default App
