import badass.plugin as plugin


hooked = "badass.core.push"
plugins = plugin.getPlugins()
plugin.runPreCmds(hooked, plugins)
plugin.runPostCmds(hooked, plugins)

# module = getPlugins("push")
# plugin = loadPlugin(module)
# plug = plugin.initialize()
# plug.pre(tt="tt")
# plug.post(stat=True, yop="aa")

# print getPluginsPaths()
