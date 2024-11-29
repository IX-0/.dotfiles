-- load defaults i.e lua_lsp
local nvlsp = require("configs.lspconfig")
nvlsp.defaults()

local lspconfig = require("lspconfig") 

-- EXAMPLE
local servers = { "html", "cssls", "clangd", "pyright"}

-- lsps with default config
for _, lsp in ipairs(servers) do
  lspconfig[lsp].setup {
    on_attach = nvlsp.on_attach,
    on_init = nvlsp.on_init,
    capabilities = nvlsp.capabilities,
  }
end
