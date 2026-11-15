from django.shortcuts import render
from .services import search_aircraft, DataServiceError

FIELD_LABELS = {
    "numero_matricula": "Matrícula",
    "marca_fabricante": "Fabricante",
    "modelo": "Modelo",
    "numero_serie": "N° de Serie",
    "tipo_matricula": "Tipo de Matrícula",
    "estado_matricula": "Estado",
}


def aircraft_search(request):
    query = request.GET.get("q", "").strip()
    context = {"query": query, "columns": [], "rows": [], "message": None}

    if request.GET.get("q") is not None:
        if len(query) < 2:
            context["message"] = "Escribe al menos 2 caracteres para buscar."
        else:
            try:
                results = search_aircraft(query)
            except DataServiceError:
                context["message"] = "No se pudo consultar la fuente de datos. Intenta de nuevo."
            else:
                if not results:
                    context["message"] = f"No se encontraron aeronaves para «{query}»."
                else:
                    context["columns"] = list(FIELD_LABELS.values())
                    context["rows"] = [
                        [r.get(field, "—") for field in FIELD_LABELS.keys()]
                        for r in results
                    ]
    return render(request, "aircraft/search.html", context)