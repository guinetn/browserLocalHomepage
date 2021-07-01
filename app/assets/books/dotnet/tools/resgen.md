# ResGen

main.resx
main.en.resx


static ResourceManager rm = new ResourceManager("RadioNavTrainer", Assembly.GetExecutingAssembly());
public CultureInfo cultInfo = new CultureInfo("");

private void ChangeLanguage()
{
    // optionnel :             
    if (cultInfo.Name == "")
    {
        cultInfo = new CultureInfo("en-GB");
        Thread.CurrentThread.CurrentCulture = cultInfo;
        Thread.CurrentThread.CurrentUICulture = cultInfo;
        gb_SelectLanguage.Text = "FR";
    }
    else
    {
        cultInfo = new CultureInfo("");
        Thread.CurrentThread.CurrentCulture = cultInfo;
        Thread.CurrentThread.CurrentUICulture = cultInfo;
        gb_SelectLanguage.Text = "EN";
    }

    foreach (Control c in this.Controls)
    {
        ComponentResourceManager resources = new ComponentResourceManager(typeof(main));
        resources.ApplyResources(c, c.Name);
    }
}

private void displayInfos()
{
    // avion                                            
    string Infos = "";
    int capAvion = nav_Compas1.Heading1;

    // Effets du vent
    double crossWind=0.0 , headWind=0.0;
    if (windSpeed==0)
    labelWind.Text = rm.GetString( "nt_pasvent", cultInfo );
    else
    {
    labelWind.Text = rm.GetString( "nt_vent", cultInfo ) + ": " + windFrom.ToString() + "°/" + ((int)windSpeed).ToString() + " kT";

private void Update_Langue()
{
    // Met à jour l'affichage dans la langue sélectionnée
    try
    {
    lblcmd_clavier.Text = rm.GetString( "cmd_clavier", cultInfo);
    lblcmd_obas.Text = rm.GetString( "cmd_obas", cultInfo) + " [0-" + Speeds[Speeds.Length-1].ToString()  + " kT]";
    lblcmd_droitgo.Text = rm.GetString( "cmd_droitgo", cultInfo);
    lblcmd_espace.Text = rm.GetString( "cmd_espace", cultInfo);
    lblcmd_p.Text = rm.GetString( "cmd_p", cultInfo);
