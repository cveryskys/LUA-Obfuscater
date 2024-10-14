using System;
using System.Text.RegularExpressions;
using System.Windows.Forms;

namespace LuaObfuscatorApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnObfuscate_Click(object sender, EventArgs e)
        {
            string luaInput = txtLuaInput.Text;
            string obfuscatedLua = ObfuscateLua(luaInput);
            txtLuaOutput.Text = obfuscatedLua;
        }

        private string ObfuscateLua(string luaCode)
        {
            luaCode = Regex.Replace(luaCode, @"\b(\w+)\b", m =>
            {
                return "var" + new Random().Next(1000, 9999);
            });
            return luaCode;
        }
    }
}
