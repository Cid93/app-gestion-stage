from django.shortcuts import render as drender

def render(request, template, data):
	user = request.user
	user.perms = PERMS = {}
	for p in user.get_all_permissions():
		app, name = p.split(".")
		sub = PERMS.get(app, None)
		if sub is None:
			sub = {}
			PERMS[app] = sub

		sub[name] = True
	data["user"] = user
	return drender(request, template, data)
