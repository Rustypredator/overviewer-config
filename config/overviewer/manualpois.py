# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4 filetype=python:

####################################################################################################
# Points of Interest
####################################################################################################

manualpois = [
    {
        'id':'Park',
        'x':389 ,
        'y':132,
        'z': -265,
        'name':'Spawn Tempel',
        'description':'Dies ist die heilige Stätte bei der neue Abenteurer diese Welt betreten. Man sagt sich dass uralte Technologie in diesem Tempel verborgen ist welche Abenteurer in einem einzigen Augenblick an weit entfernte Orte bringen kann.',
        'screenshots':['spawn.jpg']
    },
    {
        'id':'Park',
        'x':-302,
        'y':65,
        'z':31,
        'name':'Random Park',
        'description':'Jemand muss eine Vorliebe für Pyramiden gehabt haben, denn dieser Park ist von einer großen Glas-Pyramide umschlossen. Die Spitze wurde in Anlehnung an die alten ägypthischen Pyramiden in goldener Farbe gestrichen. Es ist wirklich nur Farbe. Es ist nicht nötig herauf zu klettern und sich selbst davon zu überzeugen. Wir möchten nicht dass sich jemand verletzt.',
        'screenshots':['park.jpg']
    },
    {
        'id':'Park',
        'x':69,
        'y':64,
        'z':132,
        'name':'Random Beach Resort',
        'description':'Es gibt Zeiten im Leben in denen man einfach eine Pause braucht, fern vom Alltag, an einem wunderschönen Sandstrand wo man nur das leise Rauschen der Wellen und das Rascheln der Palmen-Blätter hört, und natürlich den Kellner der freundlich fragt welchen Cocktail man gerne haben möchte.',
        'screenshots':['random-beach-resort.jpg']
    },
    {
        'id':'Park',
        'x':-293,
        'y':64,
        'z':-389,
        'name':'Random Beach',
        'description':'Ein Spaziergang am Strand, Baden im Meer, Entspannen in der Sonne, Beachvolleyball oder Shopping am Random Pier. Random Beach bietet all das und mehr.',
        'screenshots':['random-beach.jpg']
    },
    {
        'id':'Park',
        'x':124,
        'y':68,
        'z':28,
        'name':'Kleiner Teich',
        'description':'Am Eingang des kleines Dorfes liegt ein kleiner Teich mit einem großen Baum in der Mitte und einem kleinen Boot, welches schon seit vielen, vielen Jahren dort zu treiben scheint.',
        'screenshots':['teich.jpg']
    },
    {
        'id':'Park',
        'x':-131,
        'y':70,
        'z':-710,
        'name':'Zeltplatz',
        'description':'Was gibt es schöneres als ein Zelt auf modrig feuchtem Waldboden aufzuschlagen und am nächsten Morgen von Waldameisen geweckt zu werden die einem über das Gesicht krabbeln? Na gut. Vielleicht ist das nicht jedermanns Ding. Aber wer so etwas mag ist hier definitiv am richtigen Ort.',
        'screenshots':['zeltplatz.jpg']
    },
    {
        'id':'Public',
        'x':64,
        'y':69,
        'z':-4,
        'name':'Bibliothek',
        'description':'Bücher wurden vor der Erfindung von eBook-Readern benutzt um Wissen zu transferieren. Eine Bibliothek ist im Wesentlichen ein Aufbewahrungsraum für Bücher da es sich bei Büchern um physische Gegenstände handelt welche derzeit nicht auf einer Speicherkarte abgelegt werden können.',
        'screenshots':['bibliothek.jpg']
    },
    {
        'id':'Public',
        'x':-52,
        'y':65,
        'z':166,
        'name':'Google+ Denkmal',
        'description':'Frag einfach nicht.',
        'screenshots':['google-plus.jpg']
    },
    {
        'id':'Public',
        'x':154,
        'y':65,
        'z':245,
        'name':'Lucas Arts Denkmal',
        'description':'Das Lucas Arts Trio: Guybrush Threepwood, Henry "Nenn\' mich nicht Junior" Jones Junior, Purpur Tentakel',
        'screenshots':['lucasarts-denkmal.jpg']
    },
    {
        'id':'Public',
        'x':-172,
        'y':72,
        'z':60,
        'name':'Schaf Denkmal',
        'description':'Heil dem großen Schaf , Mutter von... eigentlich wissen wir gar nicht ob das große Schaf die Mutter von irgend jemandem ist, aber es gibt Gerüchte dass Leute bereits IM großen Schaf waren. Abartig',
        'screenshots':['schaf-denkmal.jpg']
    },
    {
        'id':'Public',
        'x':-261,
        'y':62,
        'z':-176,
        'name':'Pyramide',
        'description':'Über die Ursprünge der großen Pyramide ist nicht viel bekannt. Einige glauben sie wurde von einer antiken Zivilisation errichtet. Andere glauben sie wurde von Außerirdischen gebaut. Was denkst DU woher sie kommt?',
        'screenshots':[
            'pyramide-aussen.jpg',
            'pyramide-innen.jpg'
        ]
    },
    {
        'id':'Public',
        'x':-226,
        'y':78,
        'z':0,
        'name':'Erholungsbad',
        'description':'Gestresst? Gönn\' dir eine Pause vom harten Alltag als Minenarbeiter und nimm ein entspannendes Bad im Whirlpool, eine belebende Dusche oder genieße eine heiße reinigende Sitzung in der Sauna.',
        'screenshots':[
            'schwimmbad-aussen-1.jpg',
            'schwimmbad-aussen-2.jpg',
            'schwimmbad-aussen-3.jpg',
            'schwimmbad-innen-1.jpg',
            'schwimmbad-innen-2.jpg',
            'schwimmbad-innen-3.jpg',
            'schwimmbad-strand.jpg',
            'schwimmbad-strand-pool.jpg'
        ]
    },
    {
        'id':'Public',
        'x':148,
        'y':71,
        'z':-68,
        'name':'Random Palace',
        'description':'Wirf einen Blick auf die erstaunliche Architektur von Random Palace, erbaut im späten... verdammt. Wir haben den Tag vergessen an dem uns DERART langweilig war.',
        'screenshots':['random-palace.jpg']
    },
    {
        'id':'Public',
        'x':-46,
        'y':72,
        'z':234,
        'name':'The Dome',
        'description':'Wenn du denkst Pyramiden wären seltsam, warte mal bis du das hier gesehen hast. Es ist eine mysteriöse Glas-Kugel die aus dem Wasser schaut. Im Inneren läuft Lava unter römischen Ziffern in die Tiefe. In der Mitte befindet sich irgend eine Art Gerät. Was zum Teufel ist hier los?',
        'screenshots':['dome.jpg']
    },
    {
        'id':'Public',
        'x':306,
        'y':86,
        'z':-74,
        'name':'Kunst Galerie',
        'description':'Die Kunst Galerie welche sich auf dem Berg neben Weezer\'s Villa befindet sucht noch nach Künstlern die gerne ihre Werke dort ausstellen möchten.',
        'screenshots':['kunstgalerie.jpg']
    },
    {
        'id':'Public',
        'x':304,
        'y':69,
        'z':148,
        'name':'Kaninchen Tempel',
        'description':'Dies ist die heilige Stätte der Kaninchen-Anbeter. Dort werden regelmäßig magische Rituale durchgeführt welche Kaninchen überall in der Welt erscheinen lassen. Viele Kaninchen. Sehr viele Kaninchen. ZU VIELE KANINCHEN. MACH DASS ES AUFHÖRT!!! AAAAARGHHHH!!!!!!!',
        'screenshots':['kaninchen-tempel.jpg']
    },
    {
        'id':'Public',
        'x':-334,
        'y':64,
        'z':-445,
        'name':'Baketball Spielfeld',
        'description':'Wer sich sportlich betätigt hat was zu tun und bleibt gesund. Wie wäre es mit einer Runde Basketball?',
        'screenshots':['basketball-spielfeld.jpg']
    },
    {
        'id':'Public',
        'x':-129,
        'y':64,
        'z':-519,
        'name':'Pferderennbahn',
        'description':'Hier dreht sich alles um die entscheidende Frage: Wer hat die Nase vorn? Reitsport Fans kommen auf der Pferderennbahn voll auf ihre Kosten. Es darf gewettet werden.',
        'screenshots':['pferderennbahn.jpg']
    },
    {
        'id':'Public',
        'x':-14,
        'y':70,
        'z':-164,
        'name':'Leuchtturm',
        'description':'Man könnte denken dass Leuchttürme nach der Einführung von GPS weitgehend überflüssig geworden sind. Aber wenn das GPS Signal bei schlechtem Wetter mal weg ist freut man sich dann doch dass es sie noch gibt.',
        'screenshots':['leuchtturm.jpg']
    },
    {
        'id':'Commerce',
        'x':55,
        'y':68,
        'z':31,
        'name':'Random Mining Inc.',
        'description':'Random Mining Inc. ist allgemein bekannt als das erste Gebäude das jemals gebaut wurde. Daher steht es unter Denkmalschutz und soll bis zu dem Tag in dieser Welt verweilen, an dem der Nether zufriert.',
        'screenshots':['random-mining.jpg']
    },
    {
        'id':'Commerce',
        'x':-223,
        'y':70,
        'z':59,
        'name':'Random Office',
        'description':'Wir sind nicht gerade stolz auf diesen eher hässlichen Büro-Wolkenkratzer aber um Unternehmen in unsere kleine verträumte Welt zu locken mussten wir ihnen Büroflächen zur Verfügung stellen. Glücklicherweise befindet sich das Erholungsbad direkt nebenan. So kann man sich nach der harten Arbeit direkt wieder entspannen.',
        'screenshots':[
            'buero-aussen.jpg',
            'buero-innen-1.jpg',
            'buero-innen-2.jpg',
            'buero-innen-3.jpg',
            'buero-innen-4.jpg'
        ]
    },
    {
        'id':'Commerce',
        'x':7,
        'y':79,
        'z':-60,
        'name':'Hotel Random',
        'description':'Da eine Villa auf einem Berg offenbar nicht genug ist beantragte der selbe Typ der sie gebaut hat noch eine Genehmigung für ein Hotel an unserem wunderschönen Strand. Eigentlich wollten wir ablehnen, aber die Marketing Abteilung war der Ansicht dass Tourismus gut für uns ist, daher...',
        'screenshots':['hotel-random.jpg']
    },
    {
        'id':'Commerce',
        'x':-225,
        'y':64,
        'z':-488,
        'name':'I-Tower',
        'description':'Der I-Tower war einst das höchste Gebäude in dieser Welt. Er scheint bis heute nicht ganz fertig gestellt zu sein, wenn man sich einmal die vielen seltsamen Redstone Konstruktionen in der Nähe ansieht. Wir denken dass dort jemand versucht hat einen Aufzug zu bauen, der leider nie fertig wurde.',
        'screenshots':[
            'itower.jpg',
            'itower-aussicht.jpg'
        ]
    },
    {
        'id':'Commerce',
        'x':-226,
        'y':72,
        'z':-660,
        'name':'Windturbine',
        'description':'Wir lieben die Natur. Daher leisten wir von Random Energy Services Inc. unseren Beitrag zum Klimaschutz, mit Öko-Strom aus Windkraftwerken wie diesem hier.',
        'screenshots':['windturbine.jpg']
    },
    {
        'id':'Commerce',
        'x':-323,
        'y':63,
        'z':-554,
        'name':'Pumpstation 1',
        'description':'Einen Bergbau Betrieb zu betreiben bedeutet auch Verantwortung zu übernehmen. Daher sorgen wir von Random Mining Inc. mit Pumpstationen wie dieser dafür dass die Bewohner im Einzugsgebiet unserer Bergbauoperationen trockene Füße behalten.',
        'screenshots':[
            'pumpstation-aussen.jpg',
            'pumpstation-innen.jpg'
        ]
    },
    {
        'id':'Commerce',
        'x':-385,
        'y':64,
        'z':-485,
        'name':'Tankstelle',
        'description':'Mit den zertifizierten schadstoffarmen Krafstoffen von Random Mining Inc. wissen Sie stets genau was in ihren Tank kommt und tun dabei noch etwas für die Umwelt. Mit Random Mining Inc. in die automobile Zukunft.',
        'screenshots':['tankstelle.jpg']
    },
    {
        'id':'Commerce',
        'x':-460,
        'y':65,
        'z':-459,
        'name':'Wasseraufbereitung',
        'description':'Unter Einhaltung moderner Industriestandards und strenger Naturschutzvorschriften sorgt Random Mining Disposal Services für eine sichere Aufbereitung von Schmutzwasser in allen Bereichen.',
        'screenshots':[
            'wasseraufbereitung.jpg',
            'wasseraufbereitung-buero.jpg',
            'wasseraufbereitung-kanalisation.jpg'
        ]
    },
    {
        'id':'Commerce',
        'x':-408,
        'y':64,
        'z':-458,
        'name':'Fastfood Restaurant',
        'description':'Für den kleinen Hunger zwischendurch bietet dieses Fastfood Restaurant direkt an der Hauptstraße günstige Gerichte für jung und alt.',
        'screenshots':[
            'fastfood-aussen.jpg',
            'fastfood-drive-in.jpg',
            'fastfood-innen.jpg'
        ]
    },
    {
        'id':'Commerce',
        'x':-374,
        'y':63,
        'z':-614,
        'name':'Bauernhof und Weingut',
        'description':'Als zertifizierter Bio-Betrieb erhalten sie bei uns Gemüse, Eier, Fleisch-Produkte und alkoholische Getränke aus garantiert ökologischer Produktion.',
        'screenshots':[
            'bauer.jpg',
            'bauer-weinberg.jpg'
        ]
    },
    {
        'id':'Commerce',
        'x':-397,
        'y':63,
        'z':-515,
        'name':'Telekommunikationsunternehmen',
        'description':'Dieser Standort eines Telekommunikationsunternehmens beherbergt unter anderem den örtlichen Fernmeldeturm.',
        'screenshots':['telekom.jpg',]
    },
    {
        'id':'Commerce',
        'x':-405,
        'y':208,
        'z':-547,
        'name':'Fernmeldeturm',
        'description':'Im inhaltlich innovativen Inneren dieses famos formidablen Fernmeldeturms verbirgt sich tendenziell teure Technik und ein relativ renommiertes Restaurant.',
        'screenshots':[
            'fernmeldeturm-aussen.jpg',
            'fernmeldeturm-innen.jpg'
        ]
    },
    {
        'id':'Private',
        'x':-306,
        'y':98,
        'z':-84,
        'name':'Villa Random',
        'description':'Jemand der sich uns nur als "RandomHost" vorstellte kam zu uns und fragte nach einer Baugenehmigung für eine Art Villa auf der Spitze eines Hügels. Wir gaben sie ihm, zogen die "Bearbeitungsgebühr" ein und haben das Weite gesucht. Später erzählte man uns dass der kranke Spinner das Ding tatsächlich gebaut hat aber niemand konnte uns sagen wie sicher es dort oben ist. Das musst du dann wohl selbst herausfinden.',
        'screenshots':[
            'villa-random-aussen.jpg',
            'villa-random-innen-1.jpg',
            'villa-random-innen-2.jpg'
        ]
    },
    {
        'id':'Private',
        'x':138,
        'y':75,
        'z':70,
        'name':'Random Village',
        'description':'Es macht fast den Eindruck als ob dieses kleine Dorf über Nacht aufgetaucht wäre. Wir erinnern uns noch an die Zeit als das hier alles noch unbebautes Grasland war. Jetzt ist es ein nettes kleines Dorf mit einem eigenen Brunnen und einer kleinen Kapelle.',
        'screenshots':['dorf.jpg']
    },
    {
        'id':'Private',
        'x':237,
        'y':67,
        'z':47,
        'name':'Weezer\'s Villa',
        'description':'Weezer ist ein cooler Typ. Vielleicht haben wir ihn deshalb einen ganzen Berg abtragen lassen um seine Villa zu bauen. Tatsächlich ist besagte Villa ziemlich hübsch geworden. Über den verstecken Raum im Keller spricht er jedoch nicht gerne.',
        'screenshots':['weezers-villa.jpg']
    },
    {
        'id':'Private',
        'x':199,
        'y':63,
        'z':91,
        'name':'Weezer\'s Yacht',
        'description':'Natürlich hat Weezer auch ein eigenes Boot. Und weil ein einfaches Motorboot nicht genug ist, hat er sich gleich ein Yacht besorgt. Klar. Warum auch nicht?',
        'screenshots':['weezers-yacht.jpg']
    },
    {
        'id':'Private',
        'x':-150,
        'y':68,
        'z':97,
        'name':'Two and a Half Blocks',
        'description':'Dieses wunderschöne Strandhaus wird vermutlich von einem hedonistischen Werbemelodien-Songschreiber oder so etwas bewohnt. Jedenfalls sieht es recht teuer aus.',
        'screenshots':['two-and-a-half-blocks.jpg']
    },
    {
        'id':'Private',
        'x':-272,
        'y':95,
        'z':175,
        'name':'Jarkko\'s Festung',
        'description':'Diese Festung gehört einem Typen namens Jarkko. Wir haben ihn allerdings eine ganze Weile nicht gesehen. Sein lebloser Körper verwest wahrscheinlich irgendwo hintern diesen Mauern. Geh und finde es selbst heraus, denn wir werden ganz sicher keinen Fuß dort hinein setzen.',
        'screenshots':['jarkkos-burg.jpg']
    },
    {
        'id':'Private',
        'x':-166,
        'y':68,
        'z':181,
        'name':'Piratenbucht',
        'description':'Die Piratenbucht beheimatet die Lieblingstaverne einiger schrecklich wichtiger Piraten sowie internationale teilweise mythisch anmutende Geschäfte.',
        'screenshots':[
            'piratenbucht.jpg',
            'piratenbucht-baecker.jpg',
            'piratenbucht-scumm-bar-1.jpg',
            'piratenbucht-scumm-bar-1.jpg',
            'piratenbucht-scumm-bar-1.jpg'
        ]
    },
    {
        'id':'Private',
        'x':605,
        'y':90,
        'z':-146,
        'name':'Bergsiedlung',
        'description':'Diese verträumte kleine Bergsiedlung befindet sich seit Mitte 2020 im Aufbau. Dabei werden die meisten Gebäude nicht klassisch gebaut sondern direkt in den Fels geschlagen.',
        'screenshots':['bergsiedlung.jpg']
    },
    {
        'id':'Private',
        'x':-269,
        'y':82,
        'z':-53,
        'name':'Baumhaus',
        'description':'Dieses schnuckelige Baumhaus gehört offenbar zur Villa nebenan. Die Anbauten sind etwas weitläufiger als man von einem Baumhaus erwartet.',
        'screenshots':['baumhaus.jpg']
    },
    {
        'id':'Military',
        'x':-550,
        'y':71,
        'z':-548,
        'name':'Militärbasis',
        'description':'Der Zweck der als Bunker angelegten Militärbasis im Inneren dieses Berges unterliegt strikter Geheimhaltung. Luftaufnahmen zeigen eine schwer gepanzerte Stahlplatte an der Spitze des Berges welche möglicherweise ein Raketensilo verschließt. Mehr Informationen liegen uns leider nicht vor.',
        'screenshots':['militaerbasis-aussen.jpg']
    },
    {
        'id':'Subway',
        'x':306,
        'y':80,
        'z':-48,
        'name':'Kunst Galerie',
        'description':'Als Teil der darüber liegenden Kunst Galerie ist dieser Bahnhof sehr kompakt und im gleichen Design gehalten.',
        'screenshots':['ubahn-galerie.jpg']
    },
    {
        'id':'Subway',
        'x':213,
        'y':62,
        'z':27,
        'name':'Weezer\'s Villa',
        'description':'Als Bestandteil der Villa welche er mit dem Schienennetz verbindet wurde dieser Unterwasser-Bahnhof aus edlem Quarz und dicken Glasblöcken gebaut.',
        'screenshots':['ubahn-weezer.jpg']
    },
    {
        'id':'Subway',
        'x':19,
        'y':67,
        'z':28,
        'name':'Random Mining Inc.',
        'description':'Heute ein Durchgangsbahnhof war diese Station früher der Ausgangspunkt der ersten Bahnlinie. Das heutige Minenstollen Motiv wurde erst viel später nachgerüstet.',
        'screenshots':['ubahn-random-mining.jpg']
    },
    {
        'id':'Subway',
        'x':-189,
        'y':68,
        'z':28,
        'name':'Erholungsbad / Park',
        'description':'In Anlehnung an den oberirdischen Außenposten von Jarkko\'s Insel wurde dieser Bahnhof vollständig in Backstein-Optik gestaltet. Früher war dies der Endpunkt der Bahnlinie. Heute ist er ein Knotenpunkt an dem Nord- und Südlinie zusammen treffen.',
        'screenshots':[
            'ubahn-park-1.jpg',
            'ubahn-park-2.jpg'
        ]
    },
    {
        'id':'Subway',
        'x':-274,
        'y':67,
        'z':-102,
        'name':'Pyramide',
        'description':'Als einer der wenigen oberirdischen Bahnhöfe greift dieser Bahnhof das antike ägypthische Design der umliegenden Wüstenbauwerke auf. Er ist der letzte Bahnhof der zur "alten Welt" gezählt wird und stellt aktuell die einzige Bahnverbindung zur "neuen Welt" her.',
        'screenshots':['ubahn-pyramide.jpg']
    },
    {
        'id':'Subway',
        'x':-306,
        'y':61,
        'z':-442,
        'name':'i-Tower',
        'description':'Als erster U-Bahnhof der "neuen Welt" stellt dieser Bahnhof die derzeit einzige Anbindung an die "alte Welt" her. Außerdem stellt er den Übergang zum oberirdischen Teil des Streckennetzes der "neuen Welt" dar.',
        'screenshots':['ubahn-itower.jpg']
    },
    {
        'id':'Subway',
        'x':-445,
        'y':64,
        'z':-527,
        'name':'Militärbasis',
        'description':'Dieser oberirdische Kopfbahnhof stellt aktuell das Ende des Streckennetzes der neuen Welt dar. Zukünftige Ausbaupläne sehen jedoch eine Fortführung des Streckennetzes in Richtung Norden vor.',
        'screenshots':['ubahn-militaerbasis.jpg']
    },
    {
        'id':'Subway',
        'x':-218,
        'y':70,
        'z':161,
        'name':'Piratensiedlung',
        'description':'Im Einklang mit der Piratensiedlung welche er anbindet wurde dieser Bahnhof vorwiegend mit dunklem Holz gestaltet. Die Piratenflagge darf natürlich auch nicht fehlen.',
        'screenshots':['ubahn-piraten.jpg']
    },
    {
        'id':'Subway',
        'x':-59,
        'y':48,
        'z':211,
        'name':'Dome',
        'description':'Dieser improvisierte, temporäre Bahnhof dient der provisorischen Bahn-Anbindung des "Dome" bis über dessen weitere Erschließung entschieden wurde.',
        'screenshots':['ubahn-dome.jpg']
    },
    {
        'id':'Subway',
        'x':642,
        'y':73,
        'z':-131,
        'name':'Ostgebirge',
        'description':'Dieser Kopfbahnhof bildet das östliche Ende der Haupt-Bahnlinie, gelegen inmitten einer wunderschönen Berglandschaft.',
        'screenshots':['ubahn-ostgebirge.jpg']
    },
    {
        'id':'Subway',
        'x':319,
        'y':81,
        'z':-224,
        'name':'Spawnpunkt',
        'description':'Dieser Bahnhof in direkter Nähe des Spawnpunktes führt neue Spieler in das bevorzugte Transportmittel der Welt ein.',
        'screenshots':['ubahn-spawnpunkt.jpg']
    },
]
